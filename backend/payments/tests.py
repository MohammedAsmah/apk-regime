from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Subscription, Invoice
from django.utils import timezone

User = get_user_model()

class PaymentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="payuser", password="password123", language="english")
        self.client.force_authenticate(user=self.user)
        
        self.create_sub_url = reverse('sub-create')
        self.cancel_sub_url = reverse('sub-cancel')
        self.invoice_list_url = reverse('invoice-list')

    def test_create_subscription_success(self):
        data = {
            "plan_id": "premium",
            "payment_method_id": "tok_visa"
        }
        response = self.client.post(self.create_sub_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Subscribed to premium")
        
        # Verify user is premium
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_premium)
        
        # Verify subscription and invoice
        self.assertTrue(Subscription.objects.filter(user=self.user, plan='premium').exists())
        self.assertEqual(Invoice.objects.filter(user=self.user).count(), 1)

    def test_create_subscription_invalid_plan(self):
        data = {
            "plan_id": "invalid_plan",
            "payment_method_id": "tok_visa"
        }
        response = self.client.post(self.create_sub_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('plan_id', response.data)

    def test_cancel_subscription_success(self):
        # First create a subscription
        Subscription.objects.create(user=self.user, plan='premium', is_active=True)
        self.user.is_premium = True
        self.user.save()
        
        response = self.client.post(self.cancel_sub_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Subscription canceled")
        
        sub = Subscription.objects.get(user=self.user)
        self.assertFalse(sub.is_active)
        self.assertEqual(sub.plan, 'free')
        
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_premium)

    def test_cancel_subscription_not_found(self):
        # No subscription created for this user
        response = self.client.post(self.cancel_sub_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "No active subscription found to cancel")

    def test_invoice_list(self):
        Invoice.objects.create(user=self.user, amount=9.99, pdf_url="https://test.com/1.pdf")
        Invoice.objects.create(user=self.user, amount=29.99, pdf_url="https://test.com/2.pdf")
        
        response = self.client.get(self.invoice_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
