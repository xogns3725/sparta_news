from django.urls import path
from . import views
urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
]
