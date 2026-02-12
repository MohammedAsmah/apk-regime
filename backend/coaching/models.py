from django.db import models
from django.conf import settings

class CoachSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="coach_sessions")
    title = models.CharField(max_length=200)
    content = models.TextField()
    structured_data = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Coaching: {self.title} for {self.user.username}"
