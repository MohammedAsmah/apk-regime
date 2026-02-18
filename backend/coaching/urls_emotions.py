from django.urls import path
from . import views

urlpatterns = [
    path("session/", views.EmotionalCoachSessionView.as_view(), name="emotional_coach_session"),
]
