from django.contrib import admin
from .models import User, Route, Bus, Ticket, Payment

# Register your models here.
admin.site.register(User)
admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(Ticket) 
admin.site.register(Payment)