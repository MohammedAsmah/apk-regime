from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

# ==========================================
# 1. REGISTER SERIALIZER
# ==========================================
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "date_of_birth",
            "gender",
            "height_cm",
            "currency",
            "language",
            "timezone",
        ]

    def create(self, validated_data):
        
        validated_data["password"] = make_password(validated_data["password"])
        return User.objects.create(**validated_data)

# ==========================================
# 2. USER PROFILE SERIALIZER
# ==========================================
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "username", "email", 
            "date_of_birth", "gender", "height_cm", 
            "current_weight_kg", "target_weight_kg", "activity_level",
            "daily_calorie_goal",
            "currency", "language", "timezone", 
            "is_premium"
        ]
        
        read_only_fields = ["id", "username", "email", "is_premium", "daily_calorie_goal"]

# ==========================================
# 3. CHANGE PASSWORD SERIALIZER
# ==========================================

# old code 
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
# after debugging code 
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("كلمة المرور القديمة غير صحيحة")
        return value

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


# ==========================================
# 4. ONBOARDING SERIALIZER
# ==========================================
class OnboardingSerializer(serializers.ModelSerializer):
    """
    Utilisé uniquement lors de l'inscription pour collecter les données santé.
    """
    class Meta:
        model = User
        fields = [
            "date_of_birth", "gender", "height_cm", 
            "current_weight_kg", "target_weight_kg", "activity_level",
            "language", "timezone"
        ]
    
    def validate_date_of_birth(self, value):
        from datetime import date
        if value >= date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value