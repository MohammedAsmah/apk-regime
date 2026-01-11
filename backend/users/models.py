from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):

    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    height_cm = models.PositiveIntegerField(null=True, blank=True)
    

    current_weight_kg = models.FloatField(null=True, blank=True)
    target_weight_kg = models.FloatField(null=True, blank=True)
    
    class ActivityLevel(models.TextChoices):
        SEDENTARY = 'SED', _('Sédentaire (Peu ou pas d\'exercice)')
        LIGHT = 'LIG', _('Léger (Exercice 1-3 jours/semaine)')
        MODERATE = 'MOD', _('Modéré (Exercice 3-5 jours/semaine)')
        ACTIVE = 'ACT', _('Actif (Exercice 6-7 jours/semaine)')
        VERY_ACTIVE = 'VER', _('Très actif (Physique + Entraînement)')

    activity_level = models.CharField(
        max_length=3, 
        choices=ActivityLevel.choices, 
        default=ActivityLevel.SEDENTARY
    )
    
    daily_calorie_goal = models.PositiveIntegerField(default=2000)


    currency = models.CharField(max_length=3, default="EUR")
    language = models.CharField(max_length=20, default="en") 
    timezone = models.CharField(max_length=50, default="Europe/Paris")
    is_premium = models.BooleanField(default=False)
    premium_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username