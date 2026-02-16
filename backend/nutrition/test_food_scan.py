from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
import io
import os
import shutil
from PIL import Image

User = get_user_model()
TEMP_MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'test_media')

@override_settings(
    STORAGES={
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
    },
    MEDIA_ROOT=TEMP_MEDIA_ROOT
)
class FoodScanTests(APITestCase):
    def setUp(self):
        if not os.path.exists(TEMP_MEDIA_ROOT):
            os.makedirs(TEMP_MEDIA_ROOT)
        self.user = User.objects.create_user(username="scanuser", password="ValidPassword123!", language="en")
        login_response = self.client.post(reverse('token_obtain_pair'), {
            "username": "scanuser",
            "password": "ValidPassword123!"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')
        self.scan_url = reverse('food-scan')

    def tearDown(self):
        if os.path.exists(TEMP_MEDIA_ROOT):
            shutil.rmtree(TEMP_MEDIA_ROOT)

    def test_food_scan_success(self):
        # Default scan
        file = io.BytesIO()
        image = Image.new('RGB', (100, 100))
        image.save(file, 'jpeg')
        file.name = 'test.jpg'
        file.seek(0)
        uploaded_image = SimpleUploadedFile("test.jpg", file.read(), content_type="image/jpeg")
        response = self.client.post(self.scan_url, {"image": uploaded_image}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["total_calories"], 350)

    def test_food_scan_pizza(self):
        file = io.BytesIO()
        image = Image.new('RGB', (100, 100))
        image.save(file, 'jpeg')
        file.name = 'pizza_photo.jpg'
        file.seek(0)
        uploaded_image = SimpleUploadedFile("pizza_photo.jpg", file.read(), content_type="image/jpeg")
        response = self.client.post(self.scan_url, {"image": uploaded_image}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["recognized_foods"][0]["name"], "Pizza Margharita")
        self.assertEqual(response.data["total_calories"], 250)

    def test_food_scan_salad(self):
        file = io.BytesIO()
        image = Image.new('RGB', (100, 100))
        image.save(file, 'jpeg')
        file.name = 'salad.jpg'
        file.seek(0)
        uploaded_image = SimpleUploadedFile("salad.jpg", file.read(), content_type="image/jpeg")
        response = self.client.post(self.scan_url, {"image": uploaded_image}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["recognized_foods"][0]["name"], "Salade Verte")
        self.assertEqual(response.data["total_calories"], 50)
