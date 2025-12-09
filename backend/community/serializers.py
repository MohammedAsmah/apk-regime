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

    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'participants_count', 'is_joined']

    def get_is_joined(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.participants.filter(id=request.user.id).exists()
        return False

class JoinChallengeSerializer(serializers.Serializer):
    challenge_id = serializers.IntegerField()