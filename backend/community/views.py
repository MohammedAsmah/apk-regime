from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator

from .models import Post, Challenge
from .serializers import PostSerializer, ChallengeSerializer, JoinChallengeSerializer

# ==========================================
# 1. POSTS (GET & POST)
# ==========================================

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Community']))
class PostListCreateView(generics.ListCreateAPIView):
    """
    GET: Récupérer le fil d'actualité.
    POST: Publier un nouveau post (avec image optionnelle).
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser, FormParser] 

    @swagger_auto_schema(
        tags=['Community'],
        manual_parameters=[
            openapi.Parameter('content', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('image', openapi.IN_FORM, type=openapi.TYPE_FILE, required=False),
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ==========================================
# 2. CHALLENGES LIST (GET & POST)
# ==========================================
@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Community']))
@method_decorator(name='post', decorator=swagger_auto_schema(tags=['Community']))
class ChallengeListView(generics.ListCreateAPIView):
    """
    GET: Liste des challenges disponibles.
    POST: Créer un nouveau challenge.
    """
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Challenge.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# ==========================================
# 3. JOIN CHALLENGE (POST)
# ==========================================
class JoinChallengeView(APIView):
    """
    POST: Rejoindre un challenge spécifique.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Community'], request_body=JoinChallengeSerializer)
    def post(self, request):
        serializer = JoinChallengeSerializer(data=request.data)
        if serializer.is_valid():
            challenge_id = serializer.validated_data['challenge_id']
            try:
                challenge = Challenge.objects.get(id=challenge_id)
                if challenge.participants.filter(id=request.user.id).exists():
                    return Response({"message": "Already joined"}, status=200)
                
                challenge.participants.add(request.user)
                return Response({"message": "Challenge joined successfully"}, status=200)
            except Challenge.DoesNotExist:
                return Response({"error": "Challenge not found. Please provide a valid challenge_id."}, status=404)
        return Response(serializer.errors, status=400)