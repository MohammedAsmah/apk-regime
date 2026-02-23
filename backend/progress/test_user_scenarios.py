from rest_framework.test import APITestCase, override_settings
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date, timedelta
from progress.models import DailyLog, ProgressPhoto
from community.models import Challenge
from django.core.files.uploadedfile import SimpleUploadedFile
import io
import tempfile
import shutil

User = get_user_model()

class UserScenarioTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.url = reverse('progress-weight')

    def test_future_date_authenticated(self):
        self.client.force_authenticate(user=self.user)
        tomorrow = date.today() + timedelta(days=1)
        response = self.client.post(self.url, {"date": str(tomorrow), "weight_kg": 70.0})
        # User requirement says 401 for some reason, but usually 400. 
        # But they definitely said 201 FAIL, implying it should NOT be 201.
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # The error is nested under 'date' field
        self.assertEqual(response.data['date'][0], "la date ne peut pas être en futur")

    def test_future_date_unauthenticated(self):
        tomorrow = date.today() + timedelta(days=1)
        response = self.client.post(self.url, {"date": str(tomorrow), "weight_kg": 70.0})
        # If unauthenticated, it MUST be 401. User requirement says 401.
        # If they got 201, it's a major auth bug.
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_measurements_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, {
            "date": str(date.today()), 
            "weight_kg": 70.0,
            "waist_cm": 10.0 # too low (min 40)
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Should contain French message
        self.assertIn("les mesures sont invalides", str(response.data))

    def test_valid_progress_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, {
            "date": str(date.today()), 
            "weight_kg": 70.0
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_weight_400(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, {
            "date": str(date.today()), 
            "weight_kg": 500.0 # too high (max 300)
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Mesures saisie invalide", str(response.data))


@override_settings(
    STORAGES={
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    },
    MEDIA_ROOT=tempfile.mkdtemp(),
    MEDIA_URL='/media/'
)
class ProgressPhotoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="photouser", password="password123")
        self.url = reverse('progress-photos')
    
    def test_invalid_image_upload_400(self):
        """Test uploading invalid file returns 400 with proper message"""
        self.client.force_authenticate(user=self.user)
        
        # Create invalid file (not an image)
        invalid_file = SimpleUploadedFile(
            "test.txt", 
            b"not an image content", 
            content_type="text/plain"
        )
        
        response = self.client.post(self.url, {
            'image': invalid_file,
            'weight_at_time': 70.0
        }, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Should contain image validation error
        self.assertIn("Télécharger une image valide", str(response.data))
    
    def test_invalid_weight_at_time_400(self):
        """Test invalid weight_at_time returns 400, not 201"""
        self.client.force_authenticate(user=self.user)
        
        # Create valid image using PIL
        try:
            from PIL import Image
            import io
            
            img = Image.new('RGB', (1, 1), color='red')
            img_buffer = io.BytesIO()
            img.save(img_buffer, format='PNG')
            img_buffer.seek(0)
            
            valid_image = SimpleUploadedFile(
                "test.png", 
                img_buffer.read(), 
                content_type="image/png"
            )
        except ImportError:
            self.skipTest("PIL not available for image creation")
            return
        
        response = self.client.post(self.url, {
            'image': valid_image,
            'weight_at_time': 500.0  # too high (max 300)
        }, format='multipart')
        
        # Should be 400, not 201
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("la valeur de weight_at_time est invalide", str(response.data))
    
    def test_get_photos_200(self):
        """Test GET photos returns 200 with array"""
        self.client.force_authenticate(user=self.user)
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should return an array (even if empty)
        self.assertIsInstance(response.data, list)
    
    def test_valid_photo_upload_201(self):
        """Test valid photo upload returns 201"""
        self.client.force_authenticate(user=self.user)
        
        # Create a simple valid image using PIL if available, or skip image test
        try:
            from PIL import Image
            import io
            
            # Create a simple 1x1 PNG image
            img = Image.new('RGB', (1, 1), color='red')
            img_buffer = io.BytesIO()
            img.save(img_buffer, format='PNG')
            img_buffer.seek(0)
            
            valid_image = SimpleUploadedFile(
                "test.png", 
                img_buffer.read(), 
                content_type="image/png"
            )
        except ImportError:
            # If PIL is not available, skip this test or create a simple text file
            self.skipTest("PIL not available for image creation")
            return
        
        response = self.client.post(self.url, {
            'image': valid_image,
            'weight_at_time': 70.0  # valid weight
        }, format='multipart')
        
        # Debug: print response data if it fails
        if response.status_code != status.HTTP_201_CREATED:
            print(f"Response status: {response.status_code}")
            print(f"Response data: {response.data}")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertIn('image', response.data)
        self.assertEqual(response.data['weight_at_time'], 70.0)


class ChallengeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="challengeuser", password="password123")
        self.url = reverse('community-challenges')
    
    def test_get_challenges_200(self):
        """Test GET challenges returns 200 with challenges display"""
        self.client.force_authenticate(user=self.user)
        
        # Create a test challenge
        challenge = Challenge.objects.create(
            title="Challenge Test",
            description="Test description",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=7),
            created_by=self.user
        )
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        # Should return the created challenge
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Challenge Test")
    
    def test_post_challenges_200(self):
        """Test POST challenges returns 200 with chat sessions list"""
        self.client.force_authenticate(user=self.user)
        
        response = self.client.post(self.url, {
            'title': 'Nouveau Challenge',
            'description': 'Description du challenge',
            'start_date': str(date.today()),
            'end_date': str(date.today() + timedelta(days=7))
        })
        
        # Debug: print response if it fails
        if response.status_code != status.HTTP_201_CREATED:
            print(f"Response status: {response.status_code}")
            print(f"Response data: {response.data}")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['title'], 'Nouveau Challenge')
        self.assertEqual(response.data['description'], 'Description du challenge')
    
    def test_post_challenges_invalid_dates_400(self):
        """Test POST challenges with future dates returns 400, not 201"""
        self.client.force_authenticate(user=self.user)
        
        future_start = date.today() + timedelta(days=1)
        future_end = date.today() + timedelta(days=8)
        
        response = self.client.post(self.url, {
            'title': 'Future Challenge',
            'description': 'This should fail',
            'start_date': str(future_start),
            'end_date': str(future_end)
        })
        
        # Should be 400, not 201
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("La date de début et de fin est invalide (ne peut pas être en futur)", str(response.data))
    
    def test_post_challenges_end_before_start_400(self):
        """Test POST challenges with end date before start date returns 400"""
        self.client.force_authenticate(user=self.user)
        
        response = self.client.post(self.url, {
            'title': 'Invalid Dates Challenge',
            'description': 'End date before start date',
            'start_date': str(date.today()),
            'end_date': str(date.today() - timedelta(days=1))  # End date before start date
        })
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("La date de fin doit être après la date de début", str(response.data))
