from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from .views import (
    RegisterView, 
    MyTokenObtainPairView, 
    UserProfileView, 
    ChangePasswordView,
    OnboardingView,      
    DeleteAccountView   
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    
    path("onboarding/", OnboardingView.as_view(), name="user_onboarding"), 
    path("account/", DeleteAccountView.as_view(), name="delete_account"),   
]