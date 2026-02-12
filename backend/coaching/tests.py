from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class CoachingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="coachuser", password="SecureTestPassword123!", language="english")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "coachuser",
            "password": "SecureTestPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')

    def test_create_session(self):
        url = reverse('coach-session-list')
        data = {"title": "Weight Loss Strategy", "content": "Eat more vegetables."}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Test List
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
