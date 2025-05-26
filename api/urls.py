from brsapp.views import manage_user, manage_route, manage_bus, manage_ticket, manage_payment
from django.urls import path

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
]