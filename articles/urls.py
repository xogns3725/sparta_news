from django.urls import path
from . import views
urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("create/", views.ArticleCreateAPIView.as_view(), name="article_create"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(),
         name="article_detail")
]
