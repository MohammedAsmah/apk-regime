from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class PreferenceValidationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="prefuser", 
            password="ValidPassword123!", 
            email="pref@example.com",
            language="en"
        )
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "prefuser",
            "password": "ValidPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        self.url = reverse('user_preferences')

    # ---- GET ----
    def test_get_preferences(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ---- PUT valid ----
    def test_put_valid_preferences(self):
        response = self.client.put(self.url, {
            "unit_system": "Metric",
            "cuisine_type": "Mediterranean",
            "notifications_enabled": True
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ---- PUT invalid unit_system ----
    def test_put_invalid_unit_system(self):
        response = self.client.put(self.url, {
            "unit_system": "Galactic",
            "cuisine_type": "Mediterranean",
            "notifications_enabled": True
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("unit_system", response.data)

    # ---- PUT invalid cuisine_type ----
    def test_put_invalid_cuisine_type(self):
        response = self.client.put(self.url, {
            "unit_system": "Metric",
            "cuisine_type": "InvalidCuisine12345",
            "notifications_enabled": True
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("cuisine_type", response.data)

    # ---- PATCH valid ----
    def test_patch_valid_preferences(self):
        response = self.client.patch(self.url, {"unit_system": "Imperial"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ---- PATCH invalid unit_system ----
    def test_patch_invalid_unit_system(self):
        response = self.client.patch(self.url, {"unit_system": "Galactic"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("unit_system", response.data)

    # ---- PATCH invalid cuisine_type ----
    def test_patch_invalid_cuisine_type(self):
        response = self.client.patch(self.url, {"cuisine_type": "NotACuisine999"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("cuisine_type", response.data)
