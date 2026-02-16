from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date, timedelta

User = get_user_model()

class ProfileValidationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="profileuser", password="ValidPassword123!", language="en")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "profileuser",
            "password": "ValidPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        self.profile_url = reverse('user_profile')

    def test_update_future_dob_returns_400(self):
        tomorrow = date.today() + timedelta(days=1)
        response = self.client.put(self.profile_url, {"date_of_birth": tomorrow.strftime('%Y-%m-%d')})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_underage_returns_400(self):
        # 17 years ago
        underage_dob = date.today() - timedelta(days=17*365 + 4)
        response = self.client.put(self.profile_url, {"date_of_birth": underage_dob.strftime('%Y-%m-%d')})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_height_returns_400(self):
        response = self.client.put(self.profile_url, {"height_cm": 300})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_future_dob_returns_400(self):
        tomorrow = date.today() + timedelta(days=1)
        response = self.client.patch(self.profile_url, {"date_of_birth": tomorrow.strftime('%Y-%m-%d')})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_underage_returns_400(self):
        underage_dob = date.today() - timedelta(days=17*365 + 4)
        response = self.client.patch(self.profile_url, {"date_of_birth": underage_dob.strftime('%Y-%m-%d')})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
