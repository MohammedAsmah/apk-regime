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
    ChangePasswordSerializer, OnboardingSerializer
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

@method_decorator(name='put', decorator=swagger_auto_schema(tags=['Authentication']))
@method_decorator(name='patch', decorator=swagger_auto_schema(tags=['Authentication']))
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user

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