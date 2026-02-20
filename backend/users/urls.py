from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView, 
    MyTokenObtainPairView, 
    UserProfileView, 
    ChangePasswordView,
    OnboardingView,      
    DeleteAccountView,
    HealthProfileView,
    UserGoalView,
    UserPreferenceView,
    LogoutView
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="token_blacklist"),
    
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    
    path("onboarding/", OnboardingView.as_view(), name="user_onboarding"), 
    path("account/", DeleteAccountView.as_view(), name="delete_account"),
    
    path("health-profile/", HealthProfileView.as_view(), name="health_profile"),
    path("goals/", UserGoalView.as_view(), name="user_goals"),
    path("preferences/", UserPreferenceView.as_view(), name="user_preferences"),
]