from rest_framework import serializers
from .models import ChatSession, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'role', 'content', 'created_at']

class ChatSessionSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = ChatSession
        fields = ['id', 'session_name', 'updated_at', 'last_message']

    def get_last_message(self, obj):
        msg = obj.messages.last()
        if msg:
            return msg.content[:30] + "..."
        return ""

class ChatMessageRequestSerializer(serializers.Serializer):
    session_id = serializers.IntegerField(required=False)
    message = serializers.CharField(required=True)