from django.shortcuts import render
from .models import *
from .serializers import UserSerializer, RouteSerializer, BusSerializer, TicketSerializer, PaymentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def generic_crud_view(model, serializer_class):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def generic_api(request, pk=None):
        if pk is None:
            # List or Create
            if request.method == 'GET':
                instances = model.objects.all()
                serializer = serializer_class(instances, many=True)
                return Response(serializer.data)
            
            elif request.method == 'POST':
                serializer = serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            # Retrieve, Update, or Delete
            try:
                instance = model.objects.get(pk=pk)
            except model.DoesNotExist:
                return Response({'error': f'{model.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)

            if request.method == 'GET':
                serializer = serializer_class(instance)
                return Response(serializer.data)

            elif request.method == 'PUT':
                serializer = serializer_class(instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif request.method == 'DELETE':
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

    return generic_api



manage_user = generic_crud_view(User, UserSerializer)
manage_route = generic_crud_view(Route, RouteSerializer)
manage_bus = generic_crud_view(Bus, BusSerializer)
manage_ticket = generic_crud_view(Ticket, TicketSerializer)
manage_payment = generic_crud_view(Payment, PaymentSerializer)



# users/views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



from rest_framework import generics
from .serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

