from django.urls import path
from . import views

urlpatterns = [
    path("quick-techniques/", views.QuickTechniquesView.as_view(), name="quick_techniques"),
]
