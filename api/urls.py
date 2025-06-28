from brsapp.views import *
from django.urls import path

# users/urls.py

from django.urls import path
from brsapp.views import CustomLoginView


urlpatterns = [
    path('user/', manage_user),
    path('user/<int:pk>/', manage_user),

    path('route/', manage_route),
    path('route/<int:pk>/', manage_route),

    path('bus/', manage_bus),
    path('bus/<int:pk>/', manage_bus),

    path('ticket/', manage_ticket),
    path('ticket/<int:pk>/', manage_ticket),

    path('payment/', manage_payment),
    path('payment/<int:pk>/', manage_payment),

    path('login/', CustomLoginView.as_view(), name='custom_login'),

    path('register-user/', RegisterUserView.as_view(), name='register'),
]