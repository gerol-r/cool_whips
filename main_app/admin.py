# main_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User

# Register custom User model using UserAdmin for proper integration
admin.site.register(User, UserAdmin)

# Register the Car model


# Register other models here.
