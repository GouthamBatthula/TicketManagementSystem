from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('download_pdf/', views.download_ticket_pdf, name='download_ticket_pdf'),
   
]