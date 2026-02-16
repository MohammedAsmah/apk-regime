from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.models import UserGoal
from datetime import date, timedelta

User = get_user_model()

class ProfilePartialUpdateTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="patchuser", password="ValidPassword123!")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "patchuser",
            "password": "ValidPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        self.goals_url = reverse('user_goals')
        # Create initial goal
        UserGoal.objects.create(user=self.user, target_weight_kg=80.0, calorie_target=2500, end_date=date.today()+timedelta(days=30))

    def test_patch_goals_partial_update_success(self):
        # Update only calorie_target - should succeed
        data = {"calorie_target": 2000}
        response = self.client.patch(self.goals_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify that target_weight_kg is still 80.0
        self.assertEqual(response.data["target_weight_kg"], 80.0)
        self.assertEqual(response.data["calorie_target"], 2000)

    def test_put_goals_full_update_missing_field_fail(self):
        # Update missing target_weight_kg and end_date - should fail on PUT
        data = {"calorie_target": 3000}
        response = self.client.put(self.goals_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("target_weight_kg", response.data)
        self.assertIn("end_date", response.data)

    def test_put_goals_full_update_success(self):
        # Provide all required fields - should succeed
        data = {
            "target_weight_kg": 75.0,
            "calorie_target": 1800,
            "end_date": str(date.today() + timedelta(days=60))
        }
        response = self.client.put(self.goals_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["target_weight_kg"], 75.0)
