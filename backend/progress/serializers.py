from rest_framework import serializers
from .models import DailyLog, ProgressPhoto, Badge, UserBadge

class DailyLogSerializer(serializers.ModelSerializer):
    weight_kg = serializers.FloatField(required=True)
    calories_consumed = serializers.IntegerField(required=True, min_value=0)
    # Support both 'hips_cm' (request) and 'hip_cm' (response)
    # Using required=True here for PUT, PATCH will bypass this via partial=True
    hips_cm = serializers.FloatField(source='hip_cm', required=True, allow_null=True)
    waist_cm = serializers.FloatField(required=True, allow_null=True)
    chest_cm = serializers.FloatField(required=True, allow_null=True)
    
    class Meta:
        model = DailyLog
        fields = "__all__"
        read_only_fields = ("id", "user", "created_at", "updated_at")

    def validate_calories_consumed(self, value):
        if value > 10000:
            raise serializers.ValidationError("Calories consumed seems excessive (max 10000).")
        return value

    def validate_date(self, value):
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError("Log date cannot be in the future.")
        return value

    def validate_weight_kg(self, value):
        if value is not None and (value < 30 or value > 300):
            raise serializers.ValidationError("Weight must be between 30 and 300 kg.")
        return value

    def validate_waist_cm(self, value):
        if value is not None and (value < 40 or value > 250):
            raise serializers.ValidationError("Waist measurement must be between 40 and 250 cm.")
        return value

    def validate_hip_cm(self, value):
        if value is not None and (value < 40 or value > 250):
            raise serializers.ValidationError("Hip measurement must be between 40 and 250 cm.")
        return value

    def validate_chest_cm(self, value):
        if value is not None and (value < 40 or value > 250):
            raise serializers.ValidationError("Chest measurement must be between 40 and 250 cm.")
        return value

    def validate(self, data):
        # Prevent date change on update
        if self.instance and 'date' in data:
            if data['date'] != self.instance.date:
                raise serializers.ValidationError({"date": "The date of a daily log cannot be changed."})
        return data
    
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