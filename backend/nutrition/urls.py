from django.urls import path
from .views import (
    FoodListCreateView,
    MealPhotoScanView,
    MealPlanGenerateView,
    MealPlanDetailView,
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
    
    # /api/v1/meal-plan/<id>/
    path("meal-plan/<int:pk>/", MealPlanDetailView.as_view(), name="plan-detail"),
    
    # ---
    # Hado ma mdkourinsh f les endpoint  , walakin daroryin
    # On les garde simples
    path("meals/", MealListCreateView.as_view(), name="meal-list"),
    path("meals/<int:pk>/", MealDetailView.as_view(), name="meal-detail"),
]