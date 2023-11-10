from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (
    RegisterSerializer,
    ChangePasswordSerializer,
    UpdateUserSerializer,
)


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.set_cookie("access_token", response.data["access"], httponly=True)
        response.set_cookie("refresh_token", response.data["refresh"], httponly=True)
        return response


class MyTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.set_cookie("access_token", response.data["access"], httponly=True)
        return response


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            response = Response(status=status.HTTP_205_RESET_CONTENT)
            response.delete_cookie("access_token")
            response.delete_cookie("refresh_token")

            return response
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
