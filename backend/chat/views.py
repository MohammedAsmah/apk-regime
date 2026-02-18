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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import asyncio
from openai import AsyncOpenAI
from .serializers import ChatMessageRequestSerializer
from django.conf import settings

@method_decorator(name='post', decorator=swagger_auto_schema(tags=['Chat'], request_body=ChatMessageRequestSerializer))
class ChatMessageView(APIView):
    """
    POST: Envoie un message à l'IA et reçoit une réponse en temps réel.
    Multi-langue supporté via le prompt système du LLM.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChatMessageRequestSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data.get('message')
            session_id = serializer.validated_data.get('session_id')
            user = request.user

            # 1. Get or create session
            session = self.get_or_create_session(user, session_id)
            
            # 2. Save User Message
            Message.objects.create(session=session, role=Message.Role.USER, content=user_message)

            # 3. Call AI (Async wrapper to call from Sync view)
            ai_response = asyncio.run(self.call_llm_with_fallback(user_message))

            # 4. Save AI Response
            ai_msg = Message.objects.create(session=session, role=Message.Role.ASSISTANT, content=ai_response)

            return Response({
                "session_id": session.id,
                "user_message": user_message,
                "ai_response": ai_response,
                "created_at": ai_msg.created_at
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_or_create_session(self, user, session_id=None):
        if session_id:
            try:
                return ChatSession.objects.get(id=session_id, user=user)
            except ChatSession.DoesNotExist:
                pass
        return ChatSession.objects.create(user=user, session_name=f"Chat {user.username}")

    async def call_llm_with_fallback(self, prompt):
        try:
            client = AsyncOpenAI(
                base_url="http://localhost:11434/v1", 
                api_key="ollama",
                timeout=5.0 
            )
            response = await client.chat.completions.create(
                model="llama3.2", 
                messages=[
                    {"role": "system", "content": "You are an empathetic nutrition coach. Support multi-language requests (FR, EN, AR, etc.)."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception:
            await asyncio.sleep(0.5)
            return f"🤖 [Mock AI]: Je suis le coach IA (Simulation). Serveur LLM indisponible. J'ai bien reçu: '{prompt}'"

# ==========================
# 2. HTML TEST VIEW
# ==========================

def chat_test_view(request):
    """
    Vue simple pour afficher la page HTML de test WebSocket.
    Accessible via: /chat/test-chat/
    """
    return render(request, "chat/test.html")