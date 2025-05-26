from rest_framework import serializers
from .models import User, Route, Bus, Ticket, Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'phone_number', 'address']



class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id','departure', 'destination']



class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'name', 'total_seats', 'route']



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'bus', 'traveller', 'date', 'ticket_number']



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment 
        fields = ['id', 'traveller', 'ticket', 'amount', 'date']