from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal

# Create your models here.
class User(AbstractUser):
    # Inherit username, email, password, etc.
    coins = models.DecimalField(max_digits=10, decimal_places=2, default=5000.00)
    lottery_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
class Car(models.Model):
    TIER_CHOICES = (
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Legendary', 'Legendary'),
    )

    ACQUISITION_METHODS = (
        ('purchase', 'Purchase'),
        ('lottery', 'Lottery'),
    )

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    trim_level = models.CharField(max_length=50, blank=True, null=True)
    tier = models.CharField(max_length=20, choices=TIER_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_hidden = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="cars")
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acquired_at = models.DateTimeField(blank=True, null=True)
    acquisition_method = models.CharField(max_length=20, choices=ACQUISITION_METHODS)
    image_url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def depreciated_value(self):
        if self.purchase_price:
            return self.purchase_price * Decimal('0.80')
        return None

    def __str__(self):
        return f"{self.make} {self.model} ({self.tier})"    