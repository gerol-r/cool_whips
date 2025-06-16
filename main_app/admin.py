# main_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User
from .models import Car

# Register custom User model using UserAdmin for proper integration
admin.site.register(User, UserAdmin)

# Register the Car model
admin.site.register(Car)

# Register other models here.
