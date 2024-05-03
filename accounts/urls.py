from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import LogoutView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
