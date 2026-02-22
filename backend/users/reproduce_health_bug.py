from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
import json

User = get_user_model()

class BugReproductionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="ValidPassword123!", email="test@example.com")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "testuser",
            "password": "ValidPassword123!"
        })
        self.token = login_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.url = reverse('health_profile')

    def test_reproduce_sleep_hours_error(self):
        print("\nTesting Sleep Hours Validation...")
        # PUT
        response = self.client.put(self.url, {"sleep_hours": 25, "stress_level": "Low"})
        print(f"PUT sleep_hours=25: Status {response.status_code}, Body: {response.data}")
        
        # PATCH
        response = self.client.patch(self.url, {"sleep_hours": -5})
        print(f"PATCH sleep_hours=-5: Status {response.status_code}, Body: {response.data}")

    def test_reproduce_stress_level_error(self):
        print("\nTesting Stress Level Validation...")
        # PUT
        response = self.client.put(self.url, {"stress_level": "InvalidLevel", "sleep_hours": 8})
        print(f"PUT stress_level=InvalidLevel: Status {response.status_code}, Body: {response.data}")

    def test_reproduce_allergies_error(self):
        print("\nTesting Allergies Validation...")
        long_text = "a" * 1001
        response = self.client.put(self.url, {"allergies": long_text, "sleep_hours": 8, "stress_level": "Low"})
        print(f"PUT allergies length 1001: Status {response.status_code}, Body: {response.data}")

if __name__ == "__main__":
    import django
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    django.setup()
    from django.test import Client
    client = Client()
    user = User.objects.get_or_create(username="testuser", email="test@example.com")[0]
    user.set_password("ValidPassword123!")
    user.save()
    
    # Login manually
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    
    headers = {"HTTP_AUTHORIZATION": f"Bearer {token}"}
    url = "/api/v1/auth/health-profile/"
    
    print("\n--- MANUAL REPRODUCTION RUN ---")
    
    # Test Sleep Hours
    r1 = client.put(url, json.dumps({"sleep_hours": 25, "stress_level": "Low"}), content_type="application/json", **headers)
    print(f"PUT sleep_hours=25: Status {r1.status_code}, Body: {r1.content.decode()}")

    r2 = client.patch(url, json.dumps({"sleep_hours": -5}), content_type="application/json", **headers)
    print(f"PATCH sleep_hours=-5: Status {r2.status_code}, Body: {r2.content.decode()}")
    
    # Test Stress Level
    r3 = client.put(url, json.dumps({"stress_level": "Invalid", "sleep_hours": 8}), content_type="application/json", **headers)
    print(f"PUT stress_level=Invalid: Status {r3.status_code}, Body: {r3.content.decode()}")
