from django.urls import path
from . import views

urlpatterns = [
    path("patterns/", views.EmotionalPatternsView.as_view(), name="emotional_patterns"),
]
