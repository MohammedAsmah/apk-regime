from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import DailyLog
from datetime import date

User = get_user_model()

class ProgressTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="proguser", 
            password="SecureTestPassword123!",
            language="english"
        )
        # Force a calorie goal for adherence calculation
        self.user.daily_calorie_goal = 2000
        self.user.save()
        
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "proguser",
            "password": "SecureTestPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        
        # Create some logs
        DailyLog.objects.create(user=self.user, date="2026-02-01", weight_kg=80.0, calories_consumed=2000)
        DailyLog.objects.create(user=self.user, date=date.today(), weight_kg=78.5, calories_consumed=2100)

    def test_progress_summary(self):
        url = reverse('progress-summary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_weight_loss'], 1.5)
        self.assertIn('adherence_score', response.data)
        self.assertEqual(response.data['current_weight'], 78.5)
