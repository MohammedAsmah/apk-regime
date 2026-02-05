import os
import django
from django.conf import settings
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

User = get_user_model()
client = APIClient()

# 1. Setup User
user = User.objects.get_or_create(username='test_repro', email='test@example.com')[0]
user.set_password('password123')
user.save()
client.force_authenticate(user=user)

print("--- Testing API v1/meals ---")

# POST Test with invalid data (ID 0)
post_url = reverse('meal-list')
data_invalid = {
    "food_ids": [0],
    "name": "Invalid Meal",
    "date": str(date.today()),
    "source_photo": 0
}
response_post = client.post(post_url, data_invalid, format='json')
print(f"POST {post_url} (Invalid IDs): Status={response_post.status_code}")
print(f"Response: {response_post.data}")

# GET Test with non-existent ID
get_url_invalid = reverse('meal-detail', kwargs={'pk': 9999})
response_get = client.get(get_url_invalid)
print(f"GET {get_url_invalid} (Non-existent ID): Status={response_get.status_code}")

# GET Test with another user's ID
other_user = User.objects.get_or_create(username='other_user')[0]
from nutrition.models import Meal
other_meal = Meal.objects.create(user=other_user, name="Other Meal", date=date.today())
get_url_other = reverse('meal-detail', kwargs={'pk': other_meal.id})
response_get_other = client.get(get_url_other)
print(f"GET {get_url_other} (Other User's Meal): Status={response_get_other.status_code}")

# POST Test with valid data
from nutrition.models import Food
food = Food.objects.create(name="Test Food", calories=100, protein=10, carbs=10, fat=10)
data_valid = {
    "food_ids": [food.id],
    "name": "Valid Meal",
    "date": str(date.today())
}
response_post_valid = client.post(post_url, data_valid, format='json')
print(f"POST {post_url} (Valid Data): Status={response_post_valid.status_code}")
if response_post_valid.status_code == 201:
    meal_id = response_post_valid.data['id']
    print(f"Created Meal ID: {meal_id}")
    
    # GET Valid
    get_url_valid = reverse('meal-detail', kwargs={'pk': meal_id})
    response_get_valid = client.get(get_url_valid)
    print(f"GET {get_url_valid} (Own Meal): Status={response_get_valid.status_code}")
