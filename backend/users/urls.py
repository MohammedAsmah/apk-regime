from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from .views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),

    # LOGIN = access + refresh
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # Refresh token
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Logout (blacklist refresh token)
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
