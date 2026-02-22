
# Step 1: Add CUISINE_CHOICES to UserPreference model
model_content = open('users/models.py', 'r', encoding='utf-8').read()
model_content = model_content.replace('\r\n', '\n')

old_model = '''class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    cuisine_type = models.CharField(max_length=100, blank=True, null=True)
    unit_system = models.CharField(max_length=20, choices=[('Metric', 'Metric'), ('Imperial', 'Imperial')], default='Metric')
    notifications_enabled = models.BooleanField(default=True)'''

new_model = '''class UserPreference(models.Model):
    CUISINE_CHOICES = [
        ('Mediterranean', 'Mediterranean'),
        ('Asian', 'Asian'),
        ('Western', 'Western'),
        ('Middle Eastern', 'Middle Eastern'),
        ('African', 'African'),
        ('Latin American', 'Latin American'),
        ('French', 'French'),
        ('Italian', 'Italian'),
        ('Japanese', 'Japanese'),
        ('Indian', 'Indian'),
        ('Other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    cuisine_type = models.CharField(max_length=100, choices=CUISINE_CHOICES, blank=True, null=True)
    unit_system = models.CharField(max_length=20, choices=[('Metric', 'Metric'), ('Imperial', 'Imperial')], default='Metric')
    notifications_enabled = models.BooleanField(default=True)'''

if old_model in model_content:
    updated_model = model_content.replace(old_model, new_model, 1)
    open('users/models.py', 'w', encoding='utf-8', newline='\r\n').write(updated_model)
    print('SUCCESS: model updated.')
else:
    print('ERROR: model block not found.')
    idx = model_content.find('class UserPreference')
    print(repr(model_content[idx:idx+400]))

# Step 2: Update UserPreferenceSerializer
ser_content = open('users/serializers.py', 'r', encoding='utf-8').read()
ser_content = ser_content.replace('\r\n', '\n')

old_ser = '''# ==========================================
# 7. USER PREFERENCE SERIALIZER
# ==========================================
class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = '__all__'
        read_only_fields = ['user']'''

new_ser = '''# ==========================================
# 7. USER PREFERENCE SERIALIZER
# ==========================================
class UserPreferenceSerializer(serializers.ModelSerializer):
    unit_system = serializers.ChoiceField(
        choices=[('Metric', 'Metric'), ('Imperial', 'Imperial')],
        required=False,
        allow_blank=True,
        allow_null=True,
        error_messages={
            'invalid_choice': "L'unit system est invalide",
        }
    )
    cuisine_type = serializers.ChoiceField(
        choices=UserPreference.CUISINE_CHOICES,
        required=False,
        allow_blank=True,
        allow_null=True,
        error_messages={
            'invalid_choice': 'la valeur de type de cuisine est invalide',
        }
    )

    class Meta:
        model = UserPreference
        fields = '__all__'
        read_only_fields = ['user']'''

if old_ser in ser_content:
    updated_ser = ser_content.replace(old_ser, new_ser, 1)
    open('users/serializers.py', 'w', encoding='utf-8', newline='\r\n').write(updated_ser)
    print('SUCCESS: serializer updated.')
else:
    print('ERROR: serializer block not found.')
    idx = ser_content.find('class UserPreferenceSerializer')
    print(repr(ser_content[max(0,idx-10):idx+300]))
