from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from datetime import timedelta, date

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator

from .models import DailyLog, ProgressPhoto, Badge
from .serializers import DailyLogSerializer, ProgressPhotoSerializer, ChartDataSerializer, BadgeSerializer

# ==========================================
# 1. TRACKING (Weight & Measurements)
# ==========================================
@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Progress']))
@method_decorator(name='post', decorator=swagger_auto_schema(tags=['Progress']))
class DailyLogListCreateView(generics.ListCreateAPIView):
    """
    GET: Historique complet.
    POST: Enregistrer Poids / Mensurations[cite: 211].
    """
    serializer_class = DailyLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return DailyLog.objects.none()
        return DailyLog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        log_date = serializer.validated_data.get('date', date.today())
        existing = DailyLog.objects.filter(user=self.request.user, date=log_date).first()
        if existing:
            serializer.update(existing, serializer.validated_data)
        else:
            serializer.save(user=self.request.user)

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Progress']))
@method_decorator(name='put', decorator=swagger_auto_schema(tags=['Progress']))
@method_decorator(name='patch', decorator=swagger_auto_schema(tags=['Progress']))
@method_decorator(name='delete', decorator=swagger_auto_schema(tags=['Progress']))
class DailyLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DailyLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return DailyLog.objects.none()
        return DailyLog.objects.filter(user=self.request.user)

# ==========================================
# 2. PHOTOS 
# ==========================================
@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Progress']))
class ProgressPhotoView(generics.ListCreateAPIView):
    serializer_class = ProgressPhotoSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return ProgressPhoto.objects.none()
        return ProgressPhoto.objects.filter(user=self.request.user)

    @swagger_auto_schema(
        tags=['Progress'],
        manual_parameters=[
            openapi.Parameter('image', openapi.IN_FORM, type=openapi.TYPE_FILE, required=True),
            openapi.Parameter('weight_at_time', openapi.IN_FORM, type=openapi.TYPE_NUMBER, required=False)
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ==========================================
# 3. CHART 
# ==========================================
class ProgressChartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Progress'], responses={200: ChartDataSerializer(many=True)})
    def get(self, request):
        end_date = date.today()
        start_date = end_date - timedelta(days=30)
        logs = DailyLog.objects.filter(user=request.user, date__range=[start_date, end_date]).order_by('date')
        
        data = [{"date": l.date, "weight": l.weight_kg, "calories": l.calories_consumed} for l in logs]
        return Response(data)

# ==========================================
# 4. BADGES 
# ==========================================
@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Progress']))
class BadgeListView(generics.ListAPIView):
    """
    GET: Liste des badges et statut (obtenu ou non).
    Endpoint: /api/v1/progress/badges/
    """
    serializer_class = BadgeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Badge.objects.all()