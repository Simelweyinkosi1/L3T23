from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import (
    LogoutView,
    LoginView,
)

app_name = "accounts"

urlpatterns = [
    # /accounts/
    path("signup/", views.signup, name="signup"),
    # /accounts/logout/
    path("logout/", LogoutView.as_view(), name="logout"),
    # /accounts/login/
    path(
        "login/", LoginView.as_view(template_name="accounts/login.html"), name="login"
    ),
]
