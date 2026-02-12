from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from datetime import timedelta, date
from django.db.models import Avg

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
# 3. CHART & SUMMARY
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

class ProgressSummaryView(APIView):
    """
    GET: Résumé global de progression.
    - Perte de poids totale
    - Score d'adhérence (basé sur les calories vs objectif)
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Progress'])
    def get(self, request):
        user = request.user
        logs = DailyLog.objects.filter(user=user).order_by('date')
        
        if not logs.exists():
            return Response({
                "total_weight_loss": 0,
                "adherence_score": 0,
                "message": "Start logging to see your summary!"
            })

        first_log = logs.first()
        latest_log = logs.last()
        
        total_loss = (first_log.weight_kg or 0) - (latest_log.weight_kg or 0)
        
        # Calculate adherence score (last 30 days)
        last_30_days = date.today() - timedelta(days=30)
        recent_logs = logs.filter(date__gte=last_30_days)
        
        adherence_days = 0
        total_recent_days = recent_logs.count()
        
        if total_recent_days > 0:
            for log in recent_logs:
                # Adherence = within 15% of calorie goal
                goal = user.daily_calorie_goal
                if goal > 0:
                    deviation = abs(log.calories_consumed - goal) / goal
                    if deviation <= 0.15:
                        adherence_days += 1
            
            adherence_score = (adherence_days / total_recent_days) * 100
        else:
            adherence_score = 0

        return Response({
            "total_weight_loss": round(total_loss, 2),
            "adherence_score": round(adherence_score, 1),
            "days_tracked": total_recent_days,
            "current_weight": latest_log.weight_kg
        })

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