from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .models import Subscription, Invoice
from .serializers import CreateSubSerializer, InvoiceSerializer, SubscriptionSerializer

# --- 1. CREATE SUBSCRIPTION ---
class CreateSubscriptionView(APIView):
    """
    POST: Créer un abonnement (Premium/Coaching).
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Payments'], request_body=CreateSubSerializer)
    def post(self, request):
        serializer = CreateSubSerializer(data=request.data)
        if serializer.is_valid():
            plan = serializer.validated_data['plan_id']
            
            user = request.user
            user.is_premium = True
            user.premium_until = timezone.now() + timedelta(days=30)
            user.save()

            sub, _ = Subscription.objects.get_or_create(user=user)
            sub.plan = plan
            sub.is_active = True
            sub.stripe_sub_id = "sub_fake_123"
            sub.save()

            Invoice.objects.create(
                user=user,
                amount=9.99 if plan == 'premium' else 29.99,
                pdf_url="https://nutrifit.app/invoices/fake.pdf"
            )

            return Response({
                "message": f"Subscribed to {plan}", 
                "subscription": SubscriptionSerializer(sub).data
            }, status=200)
        return Response(serializer.errors, status=400)

# --- 2. INVOICES LIST ---
@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Payments']))
class InvoiceListView(generics.ListAPIView):
    """
    GET: Historique des factures.
    """
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return Invoice.objects.none()
        return Invoice.objects.filter(user=self.request.user)

# --- 3. CANCEL SUBSCRIPTION ---
class CancelSubscriptionView(APIView):
    """
    POST: Annuler l'abonnement.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Payments'])
    def post(self, request):
        try:
            sub = Subscription.objects.get(user=request.user)
            sub.is_active = False
            sub.plan = 'free'
            sub.save()
            
            request.user.is_premium = False
            request.user.save()
            
            return Response({"message": "Subscription canceled"}, status=200)
        except Subscription.DoesNotExist:
            return Response({"message": "No active subscription found to cancel"}, status=200)