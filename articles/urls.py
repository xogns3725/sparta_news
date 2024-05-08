from django.urls import path
from . import views
urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("comment/<int:comment_pk>/", views.ArticleCommentAPIView.as_view(),name="comment_edit_or_delete"),
    path("<int:article_pk>/", views.ArticleDetailAPIView.as_view(),name="article_detail"),
    path("<int:article_pk>/comment/", views.ArticleCommentAPIView.as_view(),name="comment_create_or_list"),
]
