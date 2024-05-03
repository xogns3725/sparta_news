from django.urls import path
from .views import UserAPIView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("", UserAPIView.as_view(),name='signup'),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<str:username>/", UserAPIView.as_view(), name='user_read_or_update'),
]
