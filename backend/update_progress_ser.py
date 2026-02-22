
import os

filepath = 'progress/serializers.py'
content = open(filepath, 'r', encoding='utf-8').read()
content = content.replace('\r\n', '\n')

old_class = '''class DailyLogSerializer(serializers.ModelSerializer):
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
        return super().to_internal_value(data)'''

new_class = '''class DailyLogSerializer(serializers.ModelSerializer):
    # Support both 'hips_cm' (request) and 'hip_cm' (response) for backward compatibility
    hips_cm = serializers.FloatField(
        source='hip_cm', 
        required=False, 
        allow_null=True,
        min_value=40,
        max_value=200,
        error_messages={
            'min_value': 'les mesures sont invalides',
            'max_value': 'les mesures sont invalides',
        }
    )
    
    weight_kg = serializers.FloatField(
        required=False, 
        allow_null=True,
        min_value=30,
        max_value=300,
        error_messages={
            'min_value': 'Mesures saisie invalide',
            'max_value': 'Mesures saisie invalide',
        }
    )
    
    waist_cm = serializers.FloatField(
        required=False, 
        allow_null=True,
        min_value=40,
        max_value=200,
        error_messages={
            'min_value': 'les mesures sont invalides',
            'max_value': 'les mesures sont invalides',
        }
    )
    
    chest_cm = serializers.FloatField(
        required=False, 
        allow_null=True,
        min_value=40,
        max_value=200,
        error_messages={
            'min_value': 'les mesures sont invalides',
            'max_value': 'les mesures sont invalides',
        }
    )
    
    calories_consumed = serializers.IntegerField(
        required=False,
        min_value=0,
        max_value=10000,
        error_messages={
            'min_value': 'les mesures sont invalides',
            'max_value': 'les mesures sont invalides',
        }
    )
    
    class Meta:
        model = DailyLog
        fields = "__all__"
        read_only_fields = ("id", "user", "created_at", "updated_at")
    
    def validate_date(self, value):
        from datetime import date
        if value > date.today():
             raise serializers.ValidationError("la date ne peut pas être en futur")
        return value

    def validate(self, data):
        # On update (PUT/PATCH), prevent changing the date
        if self.instance and 'date' in data:
            if data['date'] != self.instance.date:
                raise serializers.ValidationError({"date": "Date de journal est inchangeable"})
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
        # Normalize hips_cm to hip_cm before internal value processing
        if 'hips_cm' in data and 'hip_cm' not in data:
            data['hip_cm'] = data.pop('hips_cm')
        return super().to_internal_value(data)'''

if old_class in content:
    updated = content.replace(old_class, new_class)
    open(filepath, 'w', encoding='utf-8', newline='\r\n').write(updated)
    print("SUCCESS: Updated progress/serializers.py")
else:
    print("ERROR: Could not find old_class")
    # Try partial match if failed
    if "class DailyLogSerializer" in content:
        print("Class found but block did not match exactly.")
