from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ChatSession, Message
from .serializers import ChatSessionSerializer, MessageSerializer

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

# ==========================
# 1. API REST VIEWS
# ==========================

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Chat']))
@method_decorator(name='post', decorator=swagger_auto_schema(tags=['Chat']))
class SessionListView(generics.ListCreateAPIView):
    """
    GET: Liste toutes les conversations de l'utilisateur.
    POST: Crée une nouvelle session de chat.
    """
    serializer_class = ChatSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return ChatSession.objects.none()
        return ChatSession.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Chat']))
class SessionHistoryView(generics.ListAPIView):
    """
    GET: Récupère l'historique complet des messages d'une session spécifique.
    Endpoint: /api/v1/chat/history/{id}/
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return Message.objects.none()
        
        session_id = self.kwargs['pk']
        return Message.objects.filter(
            session_id=session_id, 
            session__user=self.request.user
        )

# ==========================
# 2. HTML TEST VIEW
# ==========================

def chat_test_view(request):
    """
    Vue simple pour afficher la page HTML de test WebSocket.
    Accessible via: /chat/test-chat/
    """
    return render(request, "chat/test.html")