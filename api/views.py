from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

class PublicView(APIView):
    permission_classes = [AllowAny]  # No authentication required

    def get(self, request):
        return Response({"message": "This is a public endpoint."})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # User must be authenticated

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! This is a protected endpoint."})
