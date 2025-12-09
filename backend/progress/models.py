from django.db import models
from django.conf import settings

class DailyLog(models.Model):
    """
    Tracking: Poids quotidien, mensurations hebdo.
    Source: PDF Section 2.2 Point 5.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="daily_logs")
    date = models.DateField(db_index=True)
    
    weight_kg = models.FloatField(null=True, blank=True)
   
    waist_cm = models.FloatField(null=True, blank=True, help_text="Tour de taille")
    hip_cm = models.FloatField(null=True, blank=True, help_text="Tour de hanches")
    chest_cm = models.FloatField(null=True, blank=True, help_text="Tour de poitrine")
    
    calories_consumed = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]
        unique_together = ['user', 'date']

    def __str__(self):
        return f"{self.user} - {self.date}"

class ProgressPhoto(models.Model):
    """
    Photos de progression.
    Source: PDF Section 2.2 Point 5.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="progress_photos")
    image = models.ImageField(upload_to="progress/body/")
    date = models.DateField(auto_now_add=True)
    weight_at_time = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ["-date"]

class Badge(models.Model):
    """
    Système achievements (Gamification).
    Source: PDF Section 2.2 Point 5.
    """
    name = models.CharField(max_length=100) 
    description = models.TextField()
    icon = models.ImageField(upload_to="progress/badges/", null=True, blank=True)
    criteria = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name

class UserBadge(models.Model):
    """
    Liaison User <-> Badge.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="earned_badges")
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'badge']