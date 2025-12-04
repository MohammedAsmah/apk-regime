from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    height_cm = models.PositiveIntegerField(null=True, blank=True)
    currency = models.CharField(max_length=3, default="EUR")
    language = models.CharField(max_length=5, default="en")  # en, fr, es...
    timezone = models.CharField(max_length=50, default="Europe/Paris")
    is_premium = models.BooleanField(default=False)
    premium_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

