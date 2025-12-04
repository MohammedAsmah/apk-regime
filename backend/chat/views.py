from rest_framework.views import APIView
from rest_framework.response import Response

class ConversationListView(APIView):
    def get(self, request):
        return Response({"message": "Chat history placeholder"})
