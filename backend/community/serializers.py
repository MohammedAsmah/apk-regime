from rest_framework import serializers
from .models import Post, Challenge

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'username', 'content', 'image', 'likes_count', 'created_at']
        read_only_fields = ['id', 'username', 'likes_count', 'created_at']

class ChallengeSerializer(serializers.ModelSerializer):
    participants_count = serializers.IntegerField(source='participants.count', read_only=True)
    is_joined = serializers.SerializerMethodField()
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    
    start_date = serializers.DateField(
        error_messages={'required': 'La date de début est obligatoire', 'invalid': 'format de date invalide'}
    )
    end_date = serializers.DateField(
        error_messages={'required': 'La date de fin est obligatoire', 'invalid': 'format de date invalide'}
    )

    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'participants_count', 'is_joined', 'created_by', 'created_by_username']
        read_only_fields = ['id', 'participants_count', 'is_joined', 'created_by', 'created_by_username']

    def get_is_joined(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.participants.filter(id=request.user.id).exists()
        return False
    
    def validate(self, data):
        from datetime import date
        
        # Validate that dates are not in the future for start_date only
        # end_date can be in the future since challenges can run forward
        today = date.today()
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        if start_date and start_date > today:
            raise serializers.ValidationError("La date de début et de fin est invalide (ne peut pas être en futur)")
        
        # Validate that end_date is after start_date
        if start_date and end_date and end_date < start_date:
            raise serializers.ValidationError("La date de fin doit être après la date de début")
        
        return data

class JoinChallengeSerializer(serializers.Serializer):
    challenge_id = serializers.IntegerField()