from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class LoginValidationTests(APITestCase):
    def setUp(self):
        self.login_url = reverse('token_obtain_pair')

    def test_login_short_password_returns_400(self):
        data = {
            "username": "anyuser",
            "password": "123"
        }
        response = self.client.post(self.login_url, data)
        # The user expects 400 for short passwords
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
