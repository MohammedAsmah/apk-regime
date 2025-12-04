from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()

class MealPhoto(models.Model):
    image = models.ImageField(upload_to='meals/')
    description = models.TextField(blank=True)

class DailyLog(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateField()
    foods = models.ManyToManyField(Food)
