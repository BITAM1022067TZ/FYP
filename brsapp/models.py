from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    ROLE_CHOICES = {
        "Admin": "Admin",
        "Traveller": "Traveller",
    }

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} - {self.role}"


class Route(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
       
    def __str__(self):
        return f"{self.departure} to {self.destination}"
    

class Bus(models.Model):  
    name = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    route = models.ManyToManyField(Route)
    
    def __str__(self):
        return f"{self.name}"


class Ticket(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True, blank=True)
    traveller = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'roles': 'Traveller'})
    date = models.DateTimeField()
    ticket_number = models.PositiveIntegerField()

    class Meta:
        unique_together = ('bus', 'ticket_number', 'date')

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            today = timezone.now().date()
            last_ticket = Ticket.objects.filter(bus=self.bus, date=today).order_by('-ticket_number').first()
            if last_ticket:
                self.ticket_number = last_ticket.ticket_number + 1
            else:
                self.ticket_number = 1
            self.date = today  # Ensure today's date is set

        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.traveller.username} bought a ticket for {self.bus.name} on {self.date}"
    

class Payment(models.Model):
    traveller = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'roles': 'Traveller'})
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.traveller.username} paid {self.amount} for {self.ticket.bus.name} on {self.date}"

