from django.urls import path
from auth.views import (
    RegisterView,
    MyTokenObtainPairView,
    MyTokenRefreshView,
    ChangePasswordView,
    UpdateProfileView,
    LogoutView,
    LogoutAllView,
)
from rest_framework_simplejwt.views import (
    TokenVerifyView,
)


urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", MyTokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
    path("logout_all/", LogoutAllView.as_view(), name="auth_logout_all"),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path(
        "change_password/<int:pk>/",
        ChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path(
        "update_profile/<int:pk>/",
        UpdateProfileView.as_view(),
        name="auth_update_profile",
    ),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
]
