from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .serializers import (
    RegisterSerializer, UserProfileSerializer, 
    ChangePasswordSerializer, OnboardingSerializer,
    HealthProfileSerializer, UserGoalSerializer, UserPreferenceSerializer
)
from .utils import calculate_daily_calories

User = get_user_model()

# ==========================================
# 1. AUTHENTICATION (Login, Register...)
# ==========================================

@method_decorator(name='post', decorator=swagger_auto_schema(tags=['Authentication']))
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['is_premium'] = self.user.is_premium
        data['language'] = self.user.language
        return data

@method_decorator(name='post', decorator=swagger_auto_schema(tags=['Authentication']))
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@method_decorator(name='post', decorator=swagger_auto_schema(tags=['Authentication']))
@method_decorator(name='put', decorator=swagger_auto_schema(tags=['Authentication']))
@method_decorator(name='patch', decorator=swagger_auto_schema(tags=['Authentication']))
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def post(self, request, *args, **kwargs):
        """Allow POST method as well as PUT/PATCH."""
        return self.put(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({"detail": "password changed"})

# ==========================================
# 2. USER PROFILE
# ==========================================

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['User Profile']))
@method_decorator(name='put', decorator=swagger_auto_schema(tags=['User Profile']))
@method_decorator(name='patch', decorator=swagger_auto_schema(tags=['User Profile']))
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def perform_update(self, serializer):
        user = serializer.save()
        user.daily_calorie_goal = calculate_daily_calories(user)
        user.save()

# ==========================================
# 3. EXTENDED PROFILES (Health, Goals, Prefs)
# ==========================================

class BaseProfileExtensionView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Automatically create the profile object if it doesn't exist
        model = self.serializer_class.Meta.model
        obj, created = model.objects.get_or_create(user=self.request.user)
        return obj

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['User Profile']))
@method_decorator(name='put', decorator=swagger_auto_schema(tags=['User Profile']))
@method_decorator(name='patch', decorator=swagger_auto_schema(tags=['User Profile']))
class HealthProfileView(BaseProfileExtensionView):
    serializer_class = HealthProfileSerializer

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['User Profile']))
@method_decorator(name='put', decorator=swagger_auto_schema(tags=['User Profile']))
@method_decorator(name='patch', decorator=swagger_auto_schema(tags=['User Profile']))
class UserGoalView(BaseProfileExtensionView):
    serializer_class = UserGoalSerializer

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['User Profile']))
@method_decorator(name='put', decorator=swagger_auto_schema(tags=['User Profile']))
@method_decorator(name='patch', decorator=swagger_auto_schema(tags=['User Profile']))
class UserPreferenceView(BaseProfileExtensionView):
    serializer_class = UserPreferenceSerializer

class OnboardingView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['User Profile'], request_body=OnboardingSerializer)
    def post(self, request):
        user = request.user
        serializer = OnboardingSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            calories = calculate_daily_calories(user)
            user.daily_calorie_goal = calories
            user.save()
            return Response({
                "message": "Onboarding complete", 
                "daily_calorie_goal": calories
            })
        return Response(serializer.errors, status=400)

class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['User Profile'])
    def delete(self, request):
        request.user.delete()
        return Response(status=204)

class LogoutView(APIView):
    """Custom logout view that blacklists the refresh token."""
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(tags=['Authentication'], request_body=None)
    def post(self, request):
        try:
            from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
            from rest_framework_simplejwt.tokens import RefreshToken
            from rest_framework_simplejwt.settings import api_settings
            
            # Get the refresh token from request data
            refresh = request.data.get('refresh')
            if refresh:
                token = RefreshToken(refresh)
                token.blacklist()
            
            return Response({"detail": "Successfully logged out."}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)