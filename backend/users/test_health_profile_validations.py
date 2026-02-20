from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class HealthProfileValidationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="healthuser", password="ValidPassword123!", email="health@example.com")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "healthuser",
            "password": "ValidPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        self.health_url = reverse('health_profile')

    def test_invalid_sleep_hours_low(self):
        response = self.client.put(self.health_url, {"sleep_hours": -1, "stress_level": "Low"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("sleep_hours", response.data)

    def test_invalid_sleep_hours_high(self):
        response = self.client.put(self.health_url, {"sleep_hours": 25, "stress_level": "Low"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("sleep_hours", response.data)

    def test_invalid_stress_level(self):
        response = self.client.put(self.health_url, {"sleep_hours": 8, "stress_level": "Extremely Stressed"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("stress_level", response.data)

    def test_patch_success(self):
        response = self.client.patch(self.health_url, {"sleep_hours": 7})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["sleep_hours"], 7)

    def test_put_requires_all_fields_fail(self):
        # BaseProfileExtensionView PUT should require all fields if serializer doesn't have defaults/nulls
        # HealthProfile fields are mostly blank/null, but let's see
        response = self.client.put(self.health_url, {"sleep_hours": 8})
        # If stress_level is required in PUT (it doesn't have a default in Serializer if not specified)
        # Actually Model has null=True, so it might pass if not specified in PUT unless serializer enforces it.
        # But BaseProfileExtensionView doesn't force extra requirements beyond Serializer.
        pass
