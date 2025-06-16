from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class PublicView(APIView):
    permission_classes = [AllowAny]  

    def get(self, request):
        return Response({"message": "This is a public endpoint."})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! This is a protected endpoint."})

@login_required
def profile_view(request):
    return HttpResponse(f"Welcome {request.user.username}, this is your profile!")