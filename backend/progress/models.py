from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)  # ADDED

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # ADDED
    updated_at = models.DateTimeField(auto_now=True)      # ADDED

    def __str__(self):
        return f"{self.user.username} - {self.date}"
