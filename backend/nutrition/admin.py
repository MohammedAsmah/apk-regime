from django.contrib import admin
from .models import Food, Meal, MealPlan, MealPhoto

admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(MealPlan)
admin.site.register(MealPhoto)