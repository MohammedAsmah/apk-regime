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
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # USERS
#     path("api/auth/", include("users.urls")),
    
#     # NUTRITION
#     path("api/nutrition/", include("nutrition.urls")),
    
#     # CHAT
#     path("api/chat/", include("chat.urls")),

#     # PROGRESS / DAILY LOG
#     path("api/progress/", include("progress.urls")),
# ]


# core/urls.py
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

    
    # USERS
    path("api/auth/", include("users.urls")),

    # NUTRITION
    path("api/nutrition/", include("nutrition.urls")),
    
    # CHAT
    path("api/chat/", include("chat.urls")),

    # PROGRESS
    path('api/progress/', include('progress.urls')),

    # SWAGGER
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

