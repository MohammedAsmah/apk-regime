from django.urls import path
from . import views

urlpatterns = [
    path("history/", views.ConversationListView.as_view(), name="history"),
]
