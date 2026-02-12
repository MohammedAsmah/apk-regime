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

class HealthProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="health_profile")
    allergies = models.TextField(blank=True, null=True)
    diseases = models.TextField(blank=True, null=True)
    stress_level = models.CharField(max_length=50, blank=True, null=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    activity_type = models.CharField(max_length=100, blank=True, null=True)
    religious_constraints = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Health Profile for {self.user.username}"

class UserGoal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="goal")
    target_weight_kg = models.FloatField(null=True, blank=True)
    calorie_target = models.PositiveIntegerField(null=True, blank=True)
    macro_targets = models.JSONField(default=dict, blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Goal for {self.user.username}"

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    cuisine_type = models.CharField(max_length=100, blank=True, null=True)
    unit_system = models.CharField(max_length=20, choices=[('Metric', 'Metric'), ('Imperial', 'Imperial')], default='Metric')
    notifications_enabled = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Preferences for {self.user.username}"