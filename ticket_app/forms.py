from django import forms

class TicketForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_number = forms.CharField(max_length=10, label="Mobile Number", widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    ticket_type = forms.ChoiceField(
        choices=[('regular', 'Regular'), ('vip', 'VIP')], 
        label="Ticket Type", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    event_details = forms.CharField(label="Event Details", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
