from rest_framework import serializers
from .models import DailyLog, ProgressPhoto, Badge, UserBadge

class DailyLogSerializer(serializers.ModelSerializer):
    # Field definitions with explicit error messages
    date = serializers.DateField(
        required=True,
        error_messages={'required': 'la date est obligatoire', 'invalid': 'format de date invalide'}
    )
    
    weight_kg = serializers.FloatField(
        required=True,
        min_value=30,
        max_value=300,
        error_messages={
            'required': 'le poids est obligatoire',
            'min_value': 'Mesures saisie invalide',
            'max_value': 'Mesures saisie invalide',
            'invalid': 'Mesures saisie invalide'
        }
    )
    
    # Measurements with shared error message
    MEASUREMENT_ERRORS = {
        'min_value': 'les mesures sont invalides',
        'max_value': 'les mesures sont invalides',
        'invalid': 'les mesures sont invalides'
    }
    
    waist_cm = serializers.FloatField(required=False, allow_null=True, min_value=40, max_value=200, error_messages=MEASUREMENT_ERRORS)
    hip_cm = serializers.FloatField(required=False, allow_null=True, min_value=40, max_value=200, error_messages=MEASUREMENT_ERRORS)
    hips_cm = serializers.FloatField(source='hip_cm', required=False, allow_null=True, min_value=40, max_value=200, error_messages=MEASUREMENT_ERRORS)
    chest_cm = serializers.FloatField(required=False, allow_null=True, min_value=40, max_value=200, error_messages=MEASUREMENT_ERRORS)
    
    calories_consumed = serializers.IntegerField(
        required=False,
        min_value=0,
        max_value=10000,
        error_messages={'min_value': 'les mesures sont invalides', 'max_value': 'les mesures sont invalides'}
    )
    
    class Meta:
        model = DailyLog
        fields = [
            'id', 'user', 'date', 'weight_kg', 'waist_cm', 'hip_cm', 'hips_cm',
            'chest_cm', 'calories_consumed', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ("id", "user", "created_at", "updated_at")

    def validate_date(self, value):
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError("la date ne peut pas être en futur")
        return value

    def validate(self, data):
        # 1. Date immutability on update
        if self.instance and 'date' in data:
            if data['date'] != self.instance.date:
                raise serializers.ValidationError({"date": "Date de journal est inchangeable"})
        
        # 2. Measurement range checks (redundant but safe)
        for field in ['waist_cm', 'hip_cm', 'chest_cm']:
            val = data.get(field)
            if val is not None and (val < 40 or val > 200):
                 raise serializers.ValidationError({field: "les mesures sont invalides"})
                 
        return data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if 'hip_cm' in ret:
            ret['hips_cm'] = ret['hip_cm']
        return ret


class ProgressPhotoSerializer(serializers.ModelSerializer):
    weight_at_time = serializers.FloatField(
        required=False,
        allow_null=True,
        min_value=30,
        max_value=300,
        error_messages={
            'min_value': 'la valeur de weight_at_time est invalide',
            'max_value': 'la valeur de weight_at_time est invalide',
            'invalid': 'la valeur de weight_at_time est invalide'
        }
    )
    
    image = serializers.ImageField(
        error_messages={
            'invalid_image': 'Télécharger une image valide',
            'required': 'Télécharger une image valide',
            'invalid': 'Télécharger une image valide'
        }
    )
    
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