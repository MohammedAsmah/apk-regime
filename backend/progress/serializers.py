from rest_framework import serializers
from .models import DailyLog, ProgressPhoto, Badge, UserBadge

class DailyLogSerializer(serializers.ModelSerializer):
    # Support both 'hips_cm' (request) and 'hip_cm' (response) for backward compatibility
    hips_cm = serializers.FloatField(source='hip_cm', required=False, allow_null=True)
    
    class Meta:
        model = DailyLog
        fields = "__all__"
        read_only_fields = ("id", "user", "created_at", "updated_at")
    
    def to_representation(self, instance):
        """Return hip_cm in response."""
        ret = super().to_representation(instance)
        # Ensure hip_cm is in the response
        if 'hip_cm' not in ret and 'hips_cm' in ret:
            ret['hip_cm'] = ret.pop('hips_cm')
        return ret
    
    def to_internal_value(self, data):
        """Accept both hips_cm and hip_cm in request."""
        if 'hips_cm' in data and 'hip_cm' not in data:
            data['hip_cm'] = data.pop('hips_cm')
        return super().to_internal_value(data)

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