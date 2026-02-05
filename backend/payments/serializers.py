from rest_framework import serializers
from .models import Subscription, Invoice

class CreateSubSerializer(serializers.Serializer):
    plan_id = serializers.ChoiceField(choices=['premium', 'coaching'])
    payment_method_id = serializers.CharField(max_length=100, required=False, default="tok_visa") # Token mock

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"