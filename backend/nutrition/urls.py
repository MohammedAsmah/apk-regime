from django.urls import path
from . import views

urlpatterns = [
    path("foods/", views.FoodListView.as_view(), name="food-list"),
    path("foods/search/", views.FoodSearchView.as_view(), name="food-search"),
]
