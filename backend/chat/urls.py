from django.urls import path
from . import views

urlpatterns = [
    # --- API REST (Pour Flutter) ---
    path('sessions/', views.SessionListView.as_view(), name='chat-sessions'),
    path('history/<int:pk>/', views.SessionHistoryView.as_view(), name='chat-history'),

    # --- TEST PAGE (HTML) ---
    # Hadi Dertha pour Test webSocket local
    path("test-chat/", views.chat_test_view, name="chat-test"),
]