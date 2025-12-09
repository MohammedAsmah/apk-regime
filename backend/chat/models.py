from django.db import models
from django.conf import settings

class ChatSession(models.Model):
    """
    Correspond à 'Conversation' dans le PDF Section 4.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chat_sessions"
    )
    session_name = models.CharField(max_length=200, default="New Chat")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.session_name} - {self.user}"

class Message(models.Model):
    """
    Correspond à 'Message' dans le PDF Section 4.
    """
    class Role(models.TextChoices):
        USER = 'user', 'User'
        ASSISTANT = 'assistant', 'Assistant'

    session = models.ForeignKey(
        ChatSession,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    role = models.CharField(max_length=20, choices=Role.choices) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    tokens_used = models.PositiveIntegerField(default=0) 

    class Meta:
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=['session', 'created_at']),
        ]

    def __str__(self):
        return f"{self.role}: {self.content[:20]}..."