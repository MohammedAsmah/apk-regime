
content = open('users/serializers.py', 'r', encoding='utf-8').read()
content = content.replace('\r\n', '\n')

# Locate and replace the HealthProfileSerializer block
marker_start = '# ==========================================\n# 5. HEALTH PROFILE SERIALIZER\n# ==========================================\n'
marker_end = '\n# ==========================================\n# 6. USER GOAL SERIALIZER'

start_idx = content.find(marker_start)
end_idx = content.find(marker_end)

if start_idx == -1 or end_idx == -1:
    print(f"ERROR: Could not find markers. start_idx={start_idx}, end_idx={end_idx}")
    print("Searching for class...")
    idx = content.find('class HealthProfileSerializer')
    print(repr(content[max(0, idx-200):idx+100]))
else:
    new_block = '''# ==========================================
# 5. HEALTH PROFILE SERIALIZER
# ==========================================
class HealthProfileSerializer(serializers.ModelSerializer):
    sleep_hours = serializers.FloatField(
        required=False,
        allow_null=True,
        min_value=0,
        max_value=24,
        error_messages={
            'min_value': 'valeur de nombres des heures de sommeil est invalide',
            'max_value': 'valeur de nombres des heures de sommeil est invalide',
        }
    )
    stress_level = serializers.ChoiceField(
        choices=HealthProfile.STRESS_CHOICES,
        required=False,
        allow_blank=True,
        allow_null=True,
        error_messages={
            'invalid_choice': 'valeur niveau de stress est invalide',
        }
    )

    class Meta:
        model = HealthProfile
        fields = '__all__'
        read_only_fields = ['user']

    def validate_allergies(self, value):
        if value and len(value) > 1000:
            raise serializers.ValidationError(
                "la valeur d'allergie et de maladies saisir est invalide"
            )
        return value

    def validate_diseases(self, value):
        if value and len(value) > 1000:
            raise serializers.ValidationError(
                "la valeur d'allergie et de maladies saisir est invalide"
            )
        return value'''

    updated = content[:start_idx] + new_block + content[end_idx:]
    open('users/serializers.py', 'w', encoding='utf-8', newline='\r\n').write(updated)
    print('SUCCESS: HealthProfileSerializer updated with explicit field declarations.')
