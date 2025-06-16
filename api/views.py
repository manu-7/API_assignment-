from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .serializers import RegisterSerializer
from .tasks import send_welcome_email



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

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_welcome_email.delay(user.email)
            return Response({"message": "User registered successfully and email task queued."})
        return Response(serializer.errors, status=400)