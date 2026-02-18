"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="NutriFit API",
      default_version='v1',
      description="API documentation for NutriFit project",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- 1. USERS & AUTH ---
    path("api/v1/auth/", include("users.urls")),

    # --- 2. NUTRITION ---
   
    path('api/v1/', include('nutrition.urls')),

    # --- 3. CHAT ---
    path("chat/", include("chat.urls")),

    # --- 4. PROGRESS ---
    path("api/v1/progress/", include("progress.urls")),

    # --- 5. COMMUNITY ---
    path("api/v1/community/", include("community.urls")),

    # --- 6. PAYMENTS ---
    path("api/v1/payments/", include("payments.urls")),

    # --- 7. ANALYTICS ---
    path("api/v1/analytics/", include("analytics.urls")),

    # --- 8. COACHING ---
    path("api/v1/", include("coaching.urls_quick")),
    path("api/v1/coach-emotions/", include("coaching.urls_emotions")),
    path("api/v1/coach/", include("coaching.urls")),
    path("api/emotions/", include("coaching.urls_patterns")),

    # --- 9. SWAGGER ---
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
