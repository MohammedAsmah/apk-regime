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

# URLs
urlpatterns = [
    path("session/", CoachSessionListCreateView.as_view(), name="coach-session-list"),
]
