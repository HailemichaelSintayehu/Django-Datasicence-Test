from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import status

from users.models import CustomUser

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = CustomUser.objects.create_user(username=username, password=password)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
