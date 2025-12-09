from django.urls import path
from .views import (
    DailyLogListCreateView, DailyLogDetailView, 
    ProgressPhotoView, ProgressChartView, BadgeListView
)

urlpatterns = [
    #  /api/v1/progress/weight/ 
    # On utilise daily-log qui gère le poids ET les mensurations
    path("weight/", DailyLogListCreateView.as_view(), name="progress-weight"),
    path("daily-log/", DailyLogListCreateView.as_view(), name="progress-log-list"), 
    
    path("daily-log/<int:pk>/", DailyLogDetailView.as_view(), name="progress-log-detail"),
    
    #  /api/v1/progress/chart/ 
    path("chart/", ProgressChartView.as_view(), name="progress-chart"),
    
    #  /api/v1/progress/photos/ 
    path("photos/", ProgressPhotoView.as_view(), name="progress-photos"),
    
    #  /api/v1/progress/badges/ 
    path("badges/", BadgeListView.as_view(), name="progress-badges"),
]