from django.urls import path, inculde
from . import views
from django.contrib import admin

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include('ticket_app.urls')),  # Include the app's URLs here
    path('', views.home, name='home'),  # Home page URL
    path('create-ticket/', views.create_ticket, name='create_ticket'),  # Ticket creation page URL
    path('ticket-success/', views.ticket_success, name='ticket_success'),  # Success page URL
    path('customers/', views.customer_list, name='customer_list'),  # Customer list URL
    path('validate-ticket/<str:qr_data>/', views.validate_ticket, name='validate_ticket'),  # Ticket validation URL
]
