from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date, timedelta

User = get_user_model()

class OnboardingValidationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="onboarduser", password="ValidPassword123!", language="en")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "onboarduser",
            "password": "ValidPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        self.onboarding_url = reverse('user_onboarding')

    def test_underage_onboarding(self):
        # Set DOB to 17 years ago
        seventeen_years_ago = date.today() - timedelta(days=17*365 + 4)
        data = {"date_of_birth": seventeen_years_ago.strftime('%Y-%m-%d')}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_height_onboarding(self):
        data = {"height_cm": 300}
        response = self.client.post(self.onboarding_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
