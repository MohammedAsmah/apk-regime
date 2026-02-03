from rest_framework import serializers
from .models import Food, Meal, MealPlan, MealPhoto

class FoodSerializer(serializers.ModelSerializer):
    calories = serializers.FloatField(required=False, default=0)
    protein = serializers.FloatField(required=False, default=0)
    carbs = serializers.FloatField(required=False, default=0)
    fat = serializers.FloatField(required=False, default=0)
    portion_grams = serializers.FloatField(required=False, default=100)

    class Meta:
        model = Food
        fields = "__all__"

class MealPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPhoto
        fields = ["id", "image", "taken_at", "recognized_foods", "total_calories"]
        read_only_fields = ["taken_at", "recognized_foods", "total_calories"]

class MealSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)
    food_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Food.objects.all(), source="foods"
    )

    class Meta:
        model = Meal
        fields = "__all__"
        read_only_fields = ("id", "user", "created_at")

class MealPlanSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True, read_only=True)
    
    class Meta:
        model = MealPlan
        fields = "__all__"
        read_only_fields = ("id", "user", "created_at")

class MealPlanGenerateSerializer(serializers.Serializer):
    target_calories = serializers.IntegerField(default=2000, min_value=500, max_value=5000)
    meals_per_day = serializers.IntegerField(default=3, min_value=1, max_value=6)
    diet_type = serializers.CharField(required=False, default="balanced") 