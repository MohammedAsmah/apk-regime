from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date, timedelta

User = get_user_model()

class UserGoalValidationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="goaluser", password="ValidPassword123!", language="en")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "goaluser",
            "password": "ValidPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        self.goals_url = reverse('user_goals')

    def test_invalid_calories_low(self):
        # Calories should be positive and reasonable
        data = {"calorie_target": 100}
        response = self.client.put(self.goals_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_calories_high(self):
        data = {"calorie_target": 20000}
        response = self.client.put(self.goals_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_target_weight_low(self):
        data = {"target_weight_kg": 10}
        response = self.client.put(self.goals_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_target_weight_high(self):
        data = {"target_weight_kg": 600}
        response = self.client.put(self.goals_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_end_date_before_start_date(self):
        # start_date is auto_now_add, so it's today.
        yesterday = date.today() - timedelta(days=1)
        data = {"end_date": yesterday.strftime('%Y-%m-%d')}
        response = self.client.put(self.goals_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
