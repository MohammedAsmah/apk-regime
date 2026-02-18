# Optimized for performance and robustness - 2026-02-04
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
    MealPhotoSerializer, MealPlanGenerateSerializer,
    VoiceSearchSerializer
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
            # Analyse AI (Mock)
            # Utilise .name au lieu de .path car .path n'est pas supporté par S3
            ai_result = analyze_meal_photo_mock(scan_obj.image.name)
            
            
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
                    name=fname, 
                    defaults={
                        'calories': 100,
                        'protein': 0,
                        'carbs': 0,
                        'fat': 0
                    }
                )
                meal.foods.add(f)
            created_meals.append(meal)
            
        
        plan = MealPlan.objects.create(
            user=request.user,
            name=f"Plan {constraints.get('diet_type', 'Std')} {date.today()}",
            constraints=constraints
        )
        plan.meals.set(created_meals)
        
        return Response(MealPlanSerializer(plan).data, status=status.HTTP_201_CREATED)

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

# ==========================================
# 5. MEAL PLANS (Navigation)
# ==========================================

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Nutrition']))
class MealPlanListView(generics.ListAPIView):
    """
    GET: Historique des plans alimentaires.
    """
    serializer_class = MealPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return MealPlan.objects.none() 
        return MealPlan.objects.filter(user=self.request.user).order_by('-created_at')

@method_decorator(name='get', decorator=swagger_auto_schema(tags=['Nutrition']))
class MealPlanDetailView(generics.RetrieveAPIView):
    serializer_class = MealPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False): return MealPlan.objects.none() 
        return MealPlan.objects.filter(user=self.request.user)

class CurrentMealPlanView(APIView):
    """
    GET: Retourne le plan alimentaire le plus récent.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Nutrition'], responses={200: MealPlanSerializer})
    def get(self, request):
        plan = MealPlan.objects.filter(user=request.user).order_by('-created_at').first()
        if not plan:
            return Response({"detail": "No meal plan found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = MealPlanSerializer(plan)
        return Response(serializer.data)

# ==========================================
# 6. VOICE SEARCH (STT)
# ==========================================
class VoiceSearchView(APIView):
    """
    POST: Recherche vocale d'aliments.
    Prend un fichier audio (mock STT) ou un transcript direct.
    """
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['Nutrition'],
        request_body=VoiceSearchSerializer,
        responses={200: FoodSerializer(many=True)}
    )
    def post(self, request):
        serializer = VoiceSearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        audio = serializer.validated_data.get('audio')
        transcript = serializer.validated_data.get('transcript')

        # Mock STT Logic
        if audio and not transcript:
            transcript = "poulet" # Mock result
        
        if not transcript:
            return Response({"error": "No audio or transcript provided"}, status=400)

        # Effectuer la recherche standard
        from django.db.models import Q
        foods = Food.objects.filter(Q(name__icontains=transcript) | Q(name_fr__icontains=transcript))
        
        return Response({
            "transcript": transcript,
            "results": FoodSerializer(foods, many=True).data
        }, status=200)

# ==========================================
# 7. ADVANCED MENUS (Weekly & Cultural)
# ==========================================
class WeeklyMealPlanView(APIView):
    """
    GET: Génère un menu hebdomadaire (7 jours).
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Nutrition'], responses={200: MealPlanSerializer(many=True)})
    def get(self, request):
        # Simulation d'un plan sur 7 jours
        plans = []
        for i in range(7):
            plan = MealPlan.objects.create(
                user=request.user,
                name=f"Day {i+1} Plan",
                constraints={"budget": "low", "diet": "balanced"}
            )
            plans.append(plan)
        return Response(MealPlanSerializer(plans, many=True).data)

class CulturalMealPlanView(APIView):
    """
    GET: Menus selon contexte culturel.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Nutrition'])
    def get(self, request):
        context = request.query_params.get('context', 'Ramadan')
        menu_data = {
            "Ramadan": ["Dates", "Harira", "Chorba", "Milk", "Grilled Fish"],
            "Fêtes": ["Lamb Roast", "Special Sweets", "Festive Rice"],
            "Invitations": ["Appetizer platter", "Main stew", "Dessert"]
        }
        items = menu_data.get(context, menu_data["Ramadan"])
        return Response({
            "context": context,
            "menu_suggestion": items,
            "note": "AI suggestion based on cultural context."
        })

class FamilyLightRecipeView(APIView):
    """
    GET: Recettes familiales allégées.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=['Nutrition'])
    def get(self, request):
        recipes = [
            {"id": 1, "name": "Poulet rôti sans peau", "calories": 250},
            {"id": 2, "name": "Lasagnes aux légumes", "calories": 320},
            {"id": 3, "name": "Gratin de chou-fleur léger", "calories": 180}
        ]
        return Response(recipes)

class MealAnalyzeView(MealPhotoScanView):
    """
    Alias pour support de l'endpoint /api/v1/meals/analyze
    """
    pass
