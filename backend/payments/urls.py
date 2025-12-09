from django.urls import path
from .views import CreateSubscriptionView, CancelSubscriptionView, InvoiceListView

urlpatterns = [
    path("create-subscription/", CreateSubscriptionView.as_view(), name="sub-create"),
    path("invoices/", InvoiceListView.as_view(), name="invoice-list"),
    path("cancel-subscription/", CancelSubscriptionView.as_view(), name="sub-cancel"),
]