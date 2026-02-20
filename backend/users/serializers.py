from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.contrib.auth.password_validation import validate_password
from .models import User, HealthProfile, UserGoal, UserPreference

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

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def validate_date_of_birth(self, value):
        from datetime import date
        if not value:
            return value
        if value >= date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        
        # Age validation (18+)
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 18:
            raise serializers.ValidationError("You must be at least 18 years old to register")
        return value

    def validate_height_cm(self, value):
        if value is not None and (value < 50 or value > 250):
            raise serializers.ValidationError("Please enter a valid height between 50 and 250 cm.")
        return value

    def validate_language(self, value):
        if value and any(char.isdigit() for char in value):
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
        if value and any(char.isdigit() for char in value):
            raise serializers.ValidationError("in language  should not contain numbers.")
        return value

    def validate_date_of_birth(self, value):
        from datetime import date
        if not value: return value
        if value >= date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        # Age validation (18+)
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 18:
            raise serializers.ValidationError("You must be at least 18 years old")
        return value

    def validate_height_cm(self, value):
        if value is not None and (value < 50 or value > 250):
            raise serializers.ValidationError("Please enter a valid height between 50 and 250 cm.")
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
        if not value: return value
        if value >= date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        # Age validation (18+)
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 18:
            raise serializers.ValidationError("You must be at least 18 years old to register")
        return value

    def validate_height_cm(self, value):
        if value is not None and (value < 50 or value > 250):
            raise serializers.ValidationError("Please enter a valid height between 50 and 250 cm.")
        return value

# ==========================================
# 5. HEALTH PROFILE SERIALIZER
# ==========================================

# ==========================================
# 5. HEALTH PROFILE SERIALIZER
# ==========================================
class HealthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProfile
        fields = '__all__'
        read_only_fields = ['user']

    def validate_sleep_hours(self, value):
        if value is not None and (value < 0 or value > 24):
            raise serializers.ValidationError("Please enter a valid number of sleep hours between 0 and 24.")
        return value

    def validate_stress_level(self, value):
        if value and value not in dict(HealthProfile.STRESS_CHOICES):
             raise serializers.ValidationError(f"Invalid stress level. Choices are: {', '.join(dict(HealthProfile.STRESS_CHOICES).keys())}")
        return value

    def validate_allergies(self, value):
        if value and len(value) > 1000:
             raise serializers.ValidationError("Allergies description is too long.")
        return value

# ==========================================
# 6. USER GOAL SERIALIZER
# ==========================================
class UserGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGoal
        fields = '__all__'
        read_only_fields = ['user', 'start_date']

    def validate_calorie_target(self, value):
        if value is not None and (value < 500 or value > 10000):
            raise serializers.ValidationError("Calories should be between 500 and 10000.")
        return value

    def validate_target_weight_kg(self, value):
        if value is not None and (value < 30 or value > 500):
            raise serializers.ValidationError("Weight should be between 30 and 500 kg.")
        return value

    def validate(self, data):
        if data.get('end_date') and data.get('start_date'):
            if data['end_date'] < data['start_date']:
                 raise serializers.ValidationError("End date cannot be before start date.")
        return data

# ==========================================
# 7. USER PREFERENCE SERIALIZER
# ==========================================
class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = '__all__'
        read_only_fields = ['user']