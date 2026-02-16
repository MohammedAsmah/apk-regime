from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date, timedelta

User = get_user_model()

class ChallengeReproductionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testadmin", password="ValidPassword123!")
        self.client.force_authenticate(user=self.user)
        self.url = reverse('community-challenges')

    def test_post_challenge_future_date_fail(self):
        # The user says challenges should NOT be in the future?
        # Let's test if a future challenge currently succeeds (it probably does)
        future_date = date.today() + timedelta(days=10)
        data = {
            "title": "Future Challenge",
            "description": "This should fail according to user report",
            "start_date": str(future_date),
            "end_date": str(future_date + timedelta(days=5))
        }
        response = self.client.post(self.url, data)
        
        # Current behavior: probably 201
        # Target behavior: 400
        print(f"DEBUG: Status code for future challenge: {response.status_code}")
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_challenge_invalid_range_fail(self):
        # End date before start date
        data = {
            "title": "Invalid Range",
            "description": "End before start",
            "start_date": str(date.today()),
            "end_date": str(date.today() - timedelta(days=1))
        }
        response = self.client.post(self.url, data)
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print(f"DEBUG: Status code for invalid range: {response.status_code}")

    def test_post_challenge_success_returns_201(self):
        # Valid challenge (today/past according to user?)
        # If user says "cannot be in future", then today or yesterday should work.
        data = {
            "title": "Today Challenge",
            "description": "Valid challenge",
            "start_date": str(date.today()),
            "end_date": str(date.today())
        }
        response = self.client.post(self.url, data)
        print(f"DEBUG: Status code for valid challenge: {response.status_code}")
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
