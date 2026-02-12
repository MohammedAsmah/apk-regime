from rest_framework import serializers, generics, permissions
from .models import AnalyticsEvent
from django.urls import path
from drf_yasg.utils import swagger_auto_schema

# Serializer
class AnalyticsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsEvent
        fields = ['id', 'event_type', 'payload', 'timestamp']
        read_only_fields = ['id', 'timestamp']

# View
class AnalyticsEventCreateView(generics.CreateAPIView):
    queryset = AnalyticsEvent.objects.all()
    serializer_class = AnalyticsEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# URLs
urlpatterns = [
    path("event/", AnalyticsEventCreateView.as_view(), name="analytics-event"),
]
