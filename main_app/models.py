from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Inherit username, email, password, etc.
    coins = models.DecimalField(max_digits=10, decimal_places=2, default=5000.00)  # Set an initial coin balance as needed
    lottery_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username