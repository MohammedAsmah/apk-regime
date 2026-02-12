from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.profile_url = reverse('user_profile')
        self.test_password = "SecureTestPassword123!"
        self.user_data = {
            "username": "testuser",
            "password": self.test_password,
            "email": "test@example.com",
            "date_of_birth": "1995-01-01",
            "gender": "M",
            "height_cm": 180,
            "currency": "EUR",
            "language": "english",
            "timezone": "Europe/Paris"
        }

    def test_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login(self):
        # First register
        self.client.post(self.register_url, self.user_data)
        
        # Then login
        login_data = {
            "username": "testuser",
            "password": self.test_password
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_access_profile_with_token(self):
        # Register and login to get token
        self.client.post(self.register_url, self.user_data)
        login_response = self.client.post(self.login_url, {
            "username": "testuser",
            "password": self.test_password
        })
        token = login_response.data['access']
        
        # Access profile
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_logout(self):
        # 1. Setup: Register and Login
        self.client.post(self.register_url, self.user_data)
        login_response = self.client.post(self.login_url, {
            "username": "testuser",
            "password": self.test_password
        })
        access_token = login_response.data['access']
        refresh_token = login_response.data['refresh']
        
        # 2. Action: Logout (Blacklist Refresh Token)
        logout_url = reverse('token_blacklist')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.post(logout_url, {"refresh": refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 3. Verification: Refreshing should now fail
        refresh_url = reverse('token_refresh')
        refresh_response = self.client.post(refresh_url, {"refresh": refresh_token})
        self.assertEqual(refresh_response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # 4. Note on Profile access:
        # After logout, the ACCESS token remains valid for its lifetime (60 minutes).
        # This is expected behavior for stateless JWTs.
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        profile_response = self.client.get(self.profile_url)
        # Traditionally, this returns 200 until the token expires.
        self.assertEqual(profile_response.status_code, status.HTTP_200_OK)

class ProfileExtensionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="extuser", 
            password="SecureTestPassword123!",
            language="english"
        )
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "extuser",
            "password": "SecureTestPassword123!"
        })
        self.token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_health_profile_get_put(self):
        url = reverse('health_profile')
        # GET should create and return empty if not exists
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # PUT update
        data = {"allergies": "Peanuts", "sleep_hours": 8.5}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['allergies'], "Peanuts")
        self.assertEqual(response.data['sleep_hours'], 8.5)

    def test_user_goals_get_put(self):
        url = reverse('user_goals')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = {"target_weight_kg": 75.0, "calorie_target": 2500}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['target_weight_kg'], 75.0)

    def test_user_preferences_get_put(self):
        url = reverse('user_preferences')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = {"cuisine_type": "Mediterranean", "unit_system": "Metric"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cuisine_type'], "Mediterranean")
