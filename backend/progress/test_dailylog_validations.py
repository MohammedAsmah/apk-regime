from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date, timedelta
from .models import DailyLog

User = get_user_model()

class DailyLogValidationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="loguser", password="ValidPassword123!", language="en")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "loguser",
            "password": "ValidPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        self.list_url = reverse('progress-log-list')
        self.weight_url = reverse('progress-weight')

    def test_post_future_date_fail(self):
        tomorrow = date.today() + timedelta(days=1)
        data = {"date": str(tomorrow), "weight_kg": 70.0}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("date", response.data)

    def test_post_weight_future_fail(self):
        tomorrow = date.today() + timedelta(days=1)
        data = {"date": str(tomorrow), "weight_kg": 70.0}
        response = self.client.post(self.weight_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_weight_invalid_fail(self):
        data = {"date": str(date.today()), "weight_kg": 500} # Over 300
        response = self.client.post(self.weight_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_invalid_measurements_fail(self):
        data = {
            "date": str(date.today()),
            "weight_kg": 500, # Invalid
            "waist_cm": 10,  # Invalid
            "hip_cm": 400,   # Invalid
            "chest_cm": 5    # Invalid
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_change_date_fail(self):
        # Create a log first
        today = date.today()
        log = DailyLog.objects.create(user=self.user, date=today, weight_kg=70.0)
        url = reverse('progress-log-detail', kwargs={'pk': log.id})
        
        yesterday = today - timedelta(days=1)
        data = {"date": str(yesterday), "weight_kg": 71.0}
        response = self.client.put(url, data)
        # User says: Date de journal est inchangeable
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_duplicate_date_500_to_400(self):
        # Create two logs
        today = date.today()
        yesterday = today - timedelta(days=1)
        log_today = DailyLog.objects.create(user=self.user, date=today, weight_kg=70.0)
        log_yesterday = DailyLog.objects.create(user=self.user, date=yesterday, weight_kg=71.0)
        
        url = reverse('progress-log-detail', kwargs={'pk': log_today.id})
        # Try to change today's log date to yesterday (conflict)
        data = {"date": str(yesterday), "weight_kg": 72.0}
        response = self.client.put(url, data)
        # Should be 400, not 500
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_calories_invalid_fail(self):
        data = {"date": str(date.today()), "weight_kg": 70.0, "calories_consumed": 15000} # Over 10000
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_partial_success(self):
        # Create a log with weight and notes
        log = DailyLog.objects.create(user=self.user, date=date.today(), weight_kg=80.0, notes="Initial note")
        url = reverse('progress-log-detail', kwargs={'pk': log.id})
        
        # PATCH only the notes
        response = self.client.patch(url, {"notes": "Updated note"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["notes"], "Updated note")
        # Weight should REMAINS 80.0
        self.assertEqual(response.data["weight_kg"], 80.0)

    def test_put_full_update_missing_field_fail(self):
        # Create a log
        log = DailyLog.objects.create(user=self.user, date=date.today(), weight_kg=80.0, calories_consumed=2000)
        url = reverse('progress-log-detail', kwargs={'pk': log.id})
        
        # PUT missing weight_kg (required for Full Update)
        data = {
            "date": str(date.today()),
            "calories_consumed": 2100
            # weight_kg is MISSING
        }
        response = self.client.put(url, data)
        # Should be 400 because weight_kg is required in PUT
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("weight_kg", response.data)
