from rest_framework import serializers, generics, permissions
from .models import CoachSession
from django.urls import path
from drf_yasg.utils import swagger_auto_schema

# Serializer
class CoachSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachSession
        fields = ['id', 'title', 'content', 'structured_data', 'created_at']
        read_only_fields = ['id', 'created_at']

# Views
class CoachSessionListCreateView(generics.ListCreateAPIView):
    serializer_class = CoachSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CoachSession.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from . import views

# URLs
urlpatterns = [
    path("session/", CoachSessionListCreateView.as_view(), name="coach-session-list"),
    path("coach-emotions/session/", views.EmotionalCoachSessionView.as_view(), name="emotional-coach-session"),
    path("emotions/patterns/", views.EmotionalPatternsView.as_view(), name="emotional-patterns"),
    path("quick-techniques/", views.QuickTechniquesView.as_view(), name="quick-techniques"),
]
