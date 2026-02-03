import os
import django
from django.conf import settings
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

User = get_user_model()
client = APIClient()

def test_logout_behavior():
    # 1. Register and Login
    username = 'testlogout'
    password = 'password123'
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
        user.save()

    login_url = reverse('token_obtain_pair')
    response = client.post(login_url, {'username': username, 'password': password}, format='json')
    access_token = response.data['access']
    refresh_token = response.data['refresh']
    print(f"Logged in. Access token starts with: {access_token[:10]}...")

    # 2. Verify Profile is accessible
    profile_url = reverse('user_profile')
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
    response = client.get(profile_url)
    print(f"Profile access before logout: {response.status_code} (Expected 200)")

    # 3. Logout (Blacklist Refresh Token)
    logout_url = reverse('token_blacklist')
    response = client.post(logout_url, {'refresh': refresh_token}, format='json')
    print(f"Logout (Blacklist) response: {response.status_code} (Expected 200 or 205)")

    # 4. Try Refreshing (Should fail)
    refresh_url = reverse('token_refresh')
    response = client.post(refresh_url, {'refresh': refresh_token}, format='json')
    print(f"Refresh after logout: {response.status_code} (Expected 401/Blacklisted)")

    # 5. Verify Profile is STILL accessible with the EXISTING Access Token
    response = client.get(profile_url)
    print(f"Profile access after logout: {response.status_code} (Expected 200 because JWT is stateless)")
    if response.status_code == 200:
        print("RESULT: Access token is still valid. This is why the report says ECHOUE (Expected 401).")

if __name__ == "__main__":
    test_logout_behavior()
