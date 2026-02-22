
content = open('users/serializers.py', 'r', encoding='utf-8').read()
content = content.replace('\r\n', '\n')

old_block = '''class UserProfileSerializer(serializers.ModelSerializer):
    language = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=20,
        validators=[
            MaxLengthValidator(20),
        ]
    )
    class Meta:'''

new_block = '''class UserProfileSerializer(serializers.ModelSerializer):
    language = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=20,
        validators=[
            MaxLengthValidator(20),
        ]
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
    class Meta:'''

if old_block in content:
    updated = content.replace(old_block, new_block, 1)
    open('users/serializers.py', 'w', encoding='utf-8', newline='\r\n').write(updated)
    print('SUCCESS: UserProfileSerializer updated.')
else:
    print('ERROR: Block not found.')
    idx = content.find('class UserProfileSerializer')
    print(repr(content[idx:idx+400]))
