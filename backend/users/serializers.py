from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.contrib.auth.password_validation import validate_password

User = get_user_model()

# ==========================================
# 1. REGISTER SERIALIZER
# ==========================================
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    user_id = serializers.ReadOnlyField(source='id')
    language = serializers.CharField(
        required=False,  
        allow_blank=True,
        max_length=20,
        validators=[                                                        
            MaxLengthValidator(20),
        ]   
    )
    class Meta:
        model = User
        fields = [
            "id",
            "user_id",
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
    def validate_language(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "in language  should not contain numbers."
            )
        return value

# ==========================================
# 2. USER PROFILE SERIALIZER
# ==========================================
class UserProfileSerializer(serializers.ModelSerializer):
    language = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=20,
        validators=[
            MaxLengthValidator(20),
        ]
    )
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
    def validate_language(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "in language  should not contain numbers."
            )
        return value


# ==========================================
# 3. CHANGE PASSWORD SERIALIZER
# ==========================================

# old code 
# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)


# after debugging code 


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct.")
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
    language = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=20,
        validators=[
            MaxLengthValidator(20),
        ]
    )
    class Meta:
        model = User
        fields = [
            "date_of_birth", "gender", "height_cm", 
            "current_weight_kg", "target_weight_kg", "activity_level",
            "language", "timezone"
        ]
    def validate_language(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "in language  should not contain numbers."
            )
        return value        
    
    def validate_date_of_birth(self, value):
        from datetime import date
        if value >= date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value