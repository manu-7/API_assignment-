from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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

class SendEmailView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        user_email = request.user.email
        if user_email:
            send_welcome_email.delay(user_email) 
            return Response({"message": f"Email task has been queued for {user_email}"})
        return Response({"error": "User has no email address."}, status=400)
