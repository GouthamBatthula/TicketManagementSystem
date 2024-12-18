# ticket_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
import qrcode
import base64
from io import BytesIO
from xhtml2pdf import pisa
from .forms import TicketForm  # Ensure you have this form imported
from django.shortcuts import render

def home(request):
    return render(request, 'ticket_app/home.html')

def create_ticket(request):
    ticket_data = None  # Initialize ticket_data to None
    
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_data = form.cleaned_data
            # Save ticket data in session for later use in the PDF download
            request.session['ticket_data'] = ticket_data
            messages.success(request, 'Ticket created successfully!')
            # After form submission, render the page with ticket data
            return render(request, 'ticket_app/create_ticket.html', {'form': form, 'ticket_data': ticket_data})
    else:
        form = TicketForm()
    
    return render(request, 'ticket_app/create_ticket.html', {'form': form, 'ticket_data': ticket_data})

def download_ticket_pdf(request):
    # Retrieve ticket data from session
    ticket_data = request.session.get('ticket_data', {})
    
    if not ticket_data:
        return HttpResponse("Ticket data not found in session.", status=400)

    # Generate QR code with smaller size
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,  # Smaller box size (default is 10)
        border=2,    # Smaller border (default is 4)
    )
    qr.add_data(f"Name: {ticket_data['name']}, Mobile: {ticket_data['mobile_number']}, Age: {ticket_data['age']}, Email: {ticket_data['email']}, Ticket Type: {ticket_data['ticket_type']}, Event: {ticket_data['event_details']}")
    qr.make(fit=True)
    qr_code_img = qr.make_image(fill='black', back_color='white')
    
    # Save QR code to a buffer
    buffer = BytesIO()
    qr_code_img.save(buffer, format="PNG")
    buffer.seek(0)
    qr_code_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Render the ticket template into HTML
    html = render_to_string('ticket_app/ticket_pdf.html', {'ticket': ticket_data, 'qr_code': qr_code_base64})

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error generating PDF', content_type='text/plain')
    
    return response
