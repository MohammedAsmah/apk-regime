import os
import sys
import django

# Add current directory to path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from rest_framework.test import APIClient
from django.urls import reverse
from datetime import date, timedelta

from django.contrib.auth import get_user_model
User = get_user_model()

def reproduce():
    client = APIClient()
    user, created = User.objects.get_or_create(username="testuser", email="test@example.com")
    if created:
        user.set_password("password123")
        user.save()
    
    client.force_authenticate(user=user)
    
    url = reverse('progress-weight')
    
    # 1. Test future date
    tomorrow = date.today() + timedelta(days=1)
    print(f"Testing future date: {tomorrow}")
    response = client.post(url, {"date": str(tomorrow), "weight_kg": 70.0})
    print(f"Response status: {response.status_code}")
    print(f"Response data: {response.data}")
    
    # 2. Test invalid measurements (too low)
    print("\nTesting invalid measurements (too low): chest_cm=10")
    response = client.post(url, {"date": str(date.today()), "weight_kg": 70.0, "chest_cm": 10})
    print(f"Response status: {response.status_code}")
    print(f"Response data: {response.data}")

    # 3. Test invalid weight (too high)
    print("\nTesting invalid weight (too high): weight_kg=500")
    response = client.post(url, {"date": str(date.today()), "weight_kg": 500.0})
    print(f"Response status: {response.status_code}")
    print(f"Response data: {response.data}")

if __name__ == "__main__":
    reproduce()
