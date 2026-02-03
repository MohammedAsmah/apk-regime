from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Food, Meal, MealPlan
from datetime import date

User = get_user_model()

class NutritionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", 
            password="testpassword123",
            language="english"
        )
        self.food = Food.objects.create(
            name="Apple",
            name_fr="Pomme",
            calories=52,
            protein=0.3,
            carbs=14,
            fat=0.2
        )
        self.food_list_url = reverse('food-search')
        self.meal_list_url = reverse('meal-list')
        
        # Login to get token
        login_url = reverse('token_obtain_pair')
        response = self.client.post(login_url, {
            "username": "testuser",
            "password": "testpassword123"
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_food_search(self):
        # Search for 'Apple'
        response = self.client.get(self.food_list_url, {'search': 'Apple'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Apple')

    def test_meal_creation(self):
        meal_data = {
            "name": "Breakfast",
            "food_ids": [self.food.id],
            "date": str(date.today())
        }
        response = self.client.post(self.meal_list_url, meal_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Meal.objects.count(), 1)
        self.assertEqual(Meal.objects.get().name, 'Breakfast')

    def test_meal_list_only_owned(self):
        # Create a meal for our user
        Meal.objects.create(user=self.user, name="My Meal", date=date.today())
        
        # Create another user and a meal for them
        other_user = User.objects.create_user(username="other", password="pass", language="english")
        Meal.objects.create(user=other_user, name="Other Meal", date=date.today())
        
        response = self.client.get(self.meal_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'My Meal')

    def test_meal_plan_generation(self):
        url = reverse('plan-generate')
        data = {
            "target_calories": 2000,
            "meals_per_day": 3,
            "diet_type": "balanced"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(MealPlan.objects.count(), 1)
        # Verify that meals and foods were created
        self.assertTrue(Meal.objects.filter(user=self.user).count() >= 3)
        # Check that "Oeufs" was created as a Food item (from mock)
        self.assertTrue(Food.objects.filter(name="Oeufs").exists())
