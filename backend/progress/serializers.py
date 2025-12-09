from rest_framework import serializers
from .models import DailyLog, ProgressPhoto, Badge, UserBadge

class DailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = "__all__"
        read_only_fields = ("id", "user", "created_at", "updated_at")

class ProgressPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressPhoto
        fields = "__all__"
        read_only_fields = ("id", "user", "date")

class BadgeSerializer(serializers.ModelSerializer):
    is_earned = serializers.SerializerMethodField()

    class Meta:
        model = Badge
        fields = ['id', 'name', 'description', 'icon', 'is_earned']

    def get_is_earned(self, obj):
        user = self.context.get('request').user
        return UserBadge.objects.filter(user=user, badge=obj).exists()

class ChartDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    weight = serializers.FloatField()
    calories = serializers.IntegerField()