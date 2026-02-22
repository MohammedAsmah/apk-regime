
content = open('users/serializers.py', 'r', encoding='utf-8').read()
content = content.replace('\r\n', '\n')

old_block = '''# ==========================================
# 4. ONBOARDING SERIALIZER
# ==========================================
class OnboardingSerializer(serializers.ModelSerializer):
    """
    Utilisé uniquement lors de l\'inscription pour collecter les données santé.
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
        return value'''

new_block = '''# ==========================================
# 4. ONBOARDING SERIALIZER
# ==========================================
class OnboardingSerializer(serializers.ModelSerializer):
    """
    Utilisé uniquement lors de l\'inscription pour collecter les données santé.
    """
    language = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=20,
        validators=[
            MaxLengthValidator(20),
        ]
    )
    height_cm = serializers.IntegerField(
        required=False,
        allow_null=True,
        min_value=50,
        max_value=250,
        error_messages={
            'min_value': 'la valeur de la hauteur en cm est invalide',
            'max_value': 'la valeur de la hauteur en cm est invalide',
        }
    )
    current_weight_kg = serializers.FloatField(
        required=False,
        allow_null=True,
        min_value=20,
        max_value=500,
        error_messages={
            'min_value': 'la valeur de poids actuelle est invalide',
            'max_value': 'la valeur de poids actuelle est invalide',
        }
    )
    target_weight_kg = serializers.FloatField(
        required=False,
        allow_null=True,
        min_value=20,
        max_value=500,
        error_messages={
            'min_value': 'la valeur de poids ciblé est invalide',
            'max_value': 'la valeur de poids ciblé est invalide',
        }
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
            raise serializers.ValidationError(
                "la date de naissance indique que vous êtes moins de [COND] âge"
            )
        return value'''

if old_block in content:
    updated = content.replace(old_block, new_block, 1)
    open('users/serializers.py', 'w', encoding='utf-8', newline='\r\n').write(updated)
    print('SUCCESS: OnboardingSerializer updated.')
else:
    print('ERROR: Block not found.')
    idx = content.find('class OnboardingSerializer')
    print(repr(content[max(0,idx-10):idx+500]))
