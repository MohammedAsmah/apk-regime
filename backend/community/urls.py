from django.urls import path
from .views import PostListCreateView, ChallengeListView, JoinChallengeView

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="community-posts"),
    path("challenges/", ChallengeListView.as_view(), name="community-challenges"),
    path("challenges/join/", JoinChallengeView.as_view(), name="join-challenge"),
]