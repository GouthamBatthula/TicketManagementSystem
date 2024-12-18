from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)  # Mobile number
    age = models.IntegerField()  # Age
    email = models.EmailField()  # Email
    number_of_tickets = models.IntegerField()  # Number of tickets
    ticket_type = models.CharField(max_length=50)  # Ticket type (VIP, Regular, etc.)

    def __str__(self):
        return f"Ticket for {self.name} ({self.ticket_type})"
