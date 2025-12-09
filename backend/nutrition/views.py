from rest_framework import generics, permissions, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from datetime import date

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator

from .models import Food, Meal, MealPlan, MealPhoto
from .serializers import (
    FoodSerializer, MealSerializer, MealPlanSerializer, 
    MealPhotoSerializer, MealPlanGenerateSerializer
)
from .utils import analyze_meal_photo_mock, generate_meal_plan_mock

# ==========================================
# 1. FOOD SEARCH (Multilingue)
# ==========================================
@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Nutrition']))
@method_decorator(name='post', decorator=swagger_auto_schema(tags=['Nutrition']))
class FoodListCreateView(generics.ListCreateAPIView):
    """
    GET: Recherche aliment (?search=apple).
    POST: Créer aliment.
    """
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Food.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'name_fr']

# ==========================================
# 2. MEAL PHOTO SCAN (Vision AI)
# ==========================================
class MealPhotoScanView(APIView):
    """
    Upload photo -> Analyse AI -> Retourne aliments reconnus.
    [cite_start][cite: 199]
    """
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['Nutrition'], 
        operation_description="Upload a food image for AI analysis",
        manual_parameters=[
            openapi.Parameter(
                name="image", in_=openapi.IN_FORM, type=openapi.TYPE_FILE, 
                required=True, description="Image to scan"
            )
        ],
        responses={201: MealPhotoSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = MealPhotoSerializer(data=request.data)
        if serializer.is_valid():
            
            scan_obj = serializer.save(user=request.user)
            
           
            ai_result = analyze_meal_photo_mock(scan_obj.image.path)
            
            
            scan_obj.recognized_foods = ai_result.get('foods', [])
            scan_obj.total_calories = ai_result.get('total_calories', 0)
            scan_obj.save()
            
            return Response(MealPhotoSerializer(scan_obj).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ==========================================
# 3. MEAL PLAN GENERATOR (LLM)
# ==========================================
class MealPlanGenerateView(APIView):
    """
    Génère un plan repas via LLM.
    [cite_start][cite: 205]
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Nutrition'], request_body=MealPlanGenerateSerializer)
    def post(self, request):
        serializer = MealPlanGenerateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        constraints = serializer.validated_data
        
        
        generated_data = generate_meal_plan_mock(request.user, constraints)
        
        
        created_meals = []
        for m_data in generated_data:
            meal = Meal.objects.create(
                user=request.user,
                name=m_data['name'],
                date=date.today()
            )
            for fname in m_data.get('foods', []):
                f, _ = Food.objects.get_or_create(
                    name=fname, defaults={'calories': 100}
                )
                meal.foods.add(f)
            created_meals.append(meal)
            
        
        plan = MealPlan.objects.create(
            user=request.user,
            name=f"Plan {constraints.get('diet_type', 'Std')} {date.today()}",
            constraints=constraints
        )
        plan.meals.set(created_meals)
        
        return Response(MealPlanSerializer(plan).data)

# ==========================================
# 4. CRUD STANDARD MEALS (Tracking)
# ==========================================
@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Nutrition']))
@method_decorator(name='post', decorator=swagger_auto_schema(tags=['Nutrition']))
class MealListCreateView(generics.ListCreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return Meal.objects.none() 
        return Meal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Nutrition']))
@method_decorator(name='put', decorator=swagger_auto_schema(tags=['Nutrition']))
@method_decorator(name='patch', decorator=swagger_auto_schema(tags=['Nutrition']))
@method_decorator(name='delete', decorator=swagger_auto_schema(tags=['Nutrition']))
class MealDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return Meal.objects.none() 
        return Meal.objects.filter(user=self.request.user)

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Nutrition']))
class MealPlanDetailView(generics.RetrieveAPIView):
    serializer_class = MealPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return MealPlan.objects.none() 
        return MealPlan.objects.filter(user=self.request.user)