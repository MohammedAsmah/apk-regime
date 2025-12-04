from rest_framework.views import APIView
from rest_framework.response import Response

class FoodListView(APIView):
    def get(self, request):
        return Response({"message": "Food list placeholder"})

class FoodSearchView(APIView):
    def get(self, request):
        return Response({"message": "Food search placeholder"})
