from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from drf_yasg.utils import swagger_auto_schema
import asyncio
from openai import AsyncOpenAI

class EmotionalCoachSessionView(APIView):
    """
    POST: Soutien émotionnel (craving, plateaux, rechutes).
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Coaching'])
    def post(self, request):
        user_message = request.data.get('message', '')
        # Mock LLM response for emotional support
        prompt = f"L'utilisateur exprime : {user_message}. Fournir un soutien émotionnel court et empathique."
        
        # Simulation d'appel LLM
        response_text = f"🤖 [Coach Émotionnel]: Je comprends votre situation. Rester fort face aux {user_message} est un défi, mais vous avez les outils pour réussir. Respirez profondément."
        
        return Response({
            "response": response_text,
            "category": "support_emotionnel"
        })

class EmotionalPatternsView(APIView):
    """
    GET: Analyse des schémas émotionnels.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Coaching'])
    def get(self, request):
        patterns = [
            {"mood": "Stressé", "occurences": 5, "trigger": "Travail"},
            {"mood": "Fatigué", "occurences": 3, "trigger": "Soirée"}
        ]
        return Response({
            "patterns": patterns,
            "summary": "Votre stress semble lié au travail le soir."
        })

class QuickTechniquesView(APIView):
    """
    GET: Techniques SOS rapides.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Coaching'])
    def get(self, request):
        techniques = [
            {"name": "Respiration 4-7-8", "duration": "1 min"},
            {"name": "Marche consciente", "duration": "5 min"},
            {"name": "Verre d'eau glacé", "duration": "30 sec"}
        ]
        return Response(techniques)
