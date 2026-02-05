from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post, Challenge
from datetime import date, timedelta

User = get_user_model()

class CommunityTests(APITestCase):
    def setUp(self):
        self.test_password = "SecureTestPassword123!"
        self.user = User.objects.create_user(username="testuser", password=self.test_password, language="french")
        self.client.force_authenticate(user=self.user)
        
        self.post_list_url = reverse('community-posts')
        self.challenge_list_url = reverse('community-challenges')
        self.join_challenge_url = reverse('join-challenge')
        
        # Create a sample challenge
        self.challenge = Challenge.objects.create(
            title="Test Challenge",
            description="Test Description",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=7)
        )

    def test_post_creation(self):
        data = {"content": "Hello Community!"}
        response = self.client.post(self.post_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().content, "Hello Community!")

    def test_post_list(self):
        Post.objects.create(user=self.user, content="Post 1")
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_challenge_list(self):
        response = self.client.get(self.challenge_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Challenge")

    def test_join_challenge_success(self):
        data = {"challenge_id": self.challenge.id}
        response = self.client.post(self.join_challenge_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Challenge joined successfully")
        self.assertTrue(self.challenge.participants.filter(id=self.user.id).exists())

    def test_join_challenge_already_joined(self):
        self.challenge.participants.add(self.user)
        data = {"challenge_id": self.challenge.id}
        response = self.client.post(self.join_challenge_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Already joined")

    def test_join_challenge_not_found(self):
        data = {"challenge_id": 999}
        response = self.client.post(self.join_challenge_url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
