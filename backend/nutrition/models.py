from django.db import models
from django.conf import settings

class Food(models.Model):
  
    name = models.CharField(max_length=200, db_index=True) 
    name_fr = models.CharField(max_length=200, blank=True, null=True) 
    

    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    
    portion_grams = models.FloatField(default=100) 
    verified = models.BooleanField(default=False) 
    image = models.ImageField(upload_to="food/items/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"

class MealPhoto(models.Model):
    """
    Stocke les photos scannées par l'utilisateur pour l'analyse AI.
    Cité dans le PDF Section 4 (Modèles)
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="meal_photos")
    image = models.ImageField(upload_to="meals/scans/")
    taken_at = models.DateTimeField(auto_now_add=True)
    

    recognized_foods = models.JSONField(default=list, blank=True) 
    total_calories = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"Scan by {self.user} at {self.taken_at}"

class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="meals")
    name = models.CharField(max_length=100) 
    

    foods = models.ManyToManyField(Food, related_name="meals")
    
 
    source_photo = models.ForeignKey(MealPhoto, on_delete=models.SET_NULL, null=True, blank=True)
    
    date = models.DateField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.name} - {self.date}"

class MealPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="meal_plans")
    name = models.CharField(max_length=100)
    meals = models.ManyToManyField(Meal, related_name="meal_plans")
    

    constraints = models.JSONField(default=dict) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plan {self.name} ({self.created_at.date()})"