from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import date, timedelta

class RegistrationValidationTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.base_data = {
            "username": "validuser",
            "password": "ValidPassword123!",
            "email": "valid@example.com",
            "date_of_birth": "1990-01-01",
            "gender": "M",
            "height_cm": 175,
            "currency": "EUR",
            "language": "en",
            "timezone": "Europe/Paris"
        }

    def test_future_dob(self):
        data = self.base_data.copy()
        data["date_of_birth"] = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("date_of_birth", response.data)

    def test_underage(self):
        data = self.base_data.copy()
        # Set DOB to 17 years ago
        seventeen_years_ago = date.today() - timedelta(days=17*365 + 4) # approx 17 years
        data["date_of_birth"] = seventeen_years_ago.strftime('%Y-%m-%d')
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("date_of_birth", response.data)

    def test_short_password(self):
        data = self.base_data.copy()
        data["password"] = "short"
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)

    def test_invalid_height_low(self):
        data = self.base_data.copy()
        data["height_cm"] = 40
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("height_cm", response.data)

    def test_invalid_height_high(self):
        data = self.base_data.copy()
        data["height_cm"] = 300
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("height_cm", response.data)

    def test_valid_registration(self):
        response = self.client.post(self.register_url, self.base_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
