from django.urls import path
from .views import (
    FoodListCreateView,
    MealPhotoScanView,
    MealPlanGenerateView,
    MealPlanListView,
    MealPlanDetailView,
    CurrentMealPlanView,
    MealListCreateView,
    MealDetailView
)

urlpatterns = [
   
    #  /api/v1/food/search/
    path("food/search/", FoodListCreateView.as_view(), name="food-search"),
    
    #  /api/v1/food/scan/
    path("food/scan/", MealPhotoScanView.as_view(), name="food-scan"),
    
    
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