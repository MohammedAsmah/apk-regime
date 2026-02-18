from django.urls import path
from .views import (
    FoodListCreateView,
    MealPhotoScanView,
    MealPlanGenerateView,
    MealPlanListView,
    MealPlanDetailView,
    CurrentMealPlanView,
    MealListCreateView,
    MealDetailView,
    VoiceSearchView,
    WeeklyMealPlanView,
    CulturalMealPlanView,
    FamilyLightRecipeView,
    MealAnalyzeView
)

urlpatterns = [
   
    #  /api/v1/food/search/
    path("food/search/", FoodListCreateView.as_view(), name="food-search"),
    
    #  /api/v1/food/scan/
    path("food/scan/", MealPhotoScanView.as_view(), name="food-scan"),
    
    #  /api/v1/food/voice-search/
    path("food/voice-search/", VoiceSearchView.as_view(), name="voice-search"),
    
    # New Endpoints
    path("meal-plans/weekly/", WeeklyMealPlanView.as_view(), name="weekly-menu"),
    path("meal-plans/cultural-context/", CulturalMealPlanView.as_view(), name="cultural-menu"),
    path("meals/analyze/", MealAnalyzeView.as_view(), name="meal-analyze"),
    path("meals/family-light/", FamilyLightRecipeView.as_view(), name="family-light"),
    
    #  /api/v1/meal-plan/generate/
    path("meal-plan/generate/", MealPlanGenerateView.as_view(), name="plan-generate"),
    
    # /api/v1/meal-plan/history/ (New)
    path("meal-plan/history/", MealPlanListView.as_view(), name="plan-history"),
    
    # /api/v1/meal-plan/current/ (New)
    path("meal-plan/current/", CurrentMealPlanView.as_view(), name="plan-current"),
    
    # /api/v1/meal-plan/<id>/
    path("meal-plan/<int:pk>/", MealPlanDetailView.as_view(), name="plan-detail"),
    
    # ---
    # Hado ma mdkourinsh f les endpoint  , walakin daroryin
    # On les garde simples
    path("meals/", MealListCreateView.as_view(), name="meal-list"),
    path("meals/<int:pk>/", MealDetailView.as_view(), name="meal-detail"),
]