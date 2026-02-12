from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class AnalyticsTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="anauser", password="SecureTestPassword123!", language="english")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "anauser",
            "password": "SecureTestPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')

    def test_post_event(self):
        url = reverse('analytics-event')
        data = {"event_type": "app_open", "payload": {"platform": "android"}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
