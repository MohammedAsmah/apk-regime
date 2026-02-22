from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date, timedelta

User = get_user_model()

class OnboardingValidationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="onboarduser", password="ValidPassword123!", email="onboard@example.com", language="en")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "onboarduser",
            "password": "ValidPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        self.onboarding_url = reverse('user_onboarding')

    def test_underage_onboarding(self):
        # 17 years old → should return 400
        seventeen_years_ago = date.today() - timedelta(days=17*365 + 4)
        data = {"date_of_birth": seventeen_years_ago.strftime('%Y-%m-%d'), "language": "fr"}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("date_of_birth", response.data)

    def test_future_date_of_birth(self):
        future_date = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        data = {"date_of_birth": future_date, "language": "fr"}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("date_of_birth", response.data)

    def test_invalid_height_onboarding(self):
        # height too high → 400
        data = {"height_cm": 300, "language": "fr"}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("height_cm", response.data)

    def test_invalid_height_too_low(self):
        # height too low → 400
        data = {"height_cm": 10, "language": "fr"}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("height_cm", response.data)

    def test_invalid_current_weight(self):
        # current weight too high → 400
        data = {"current_weight_kg": 600, "language": "fr"}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("current_weight_kg", response.data)

    def test_invalid_current_weight_too_low(self):
        # current weight too low → 400
        data = {"current_weight_kg": 5, "language": "fr"}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("current_weight_kg", response.data)

    def test_invalid_target_weight(self):
        # target weight too high → 400
        data = {"target_weight_kg": 600, "language": "fr"}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("target_weight_kg", response.data)

    def test_invalid_target_weight_too_low(self):
        # target weight too low → 400
        data = {"target_weight_kg": 5, "language": "fr"}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("target_weight_kg", response.data)
