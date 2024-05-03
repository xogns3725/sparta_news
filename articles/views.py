from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import Article
from .serializers import ArticleSrializer
from accounts.models import User
# Create your views here.


class ArticleListAPIView(APIView):
    def get(self, request):  # article 리스트
        articles = Article.objects.all()
        serializer = ArticleSrializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):  # 게시글 작성
        serializer = ArticleSrializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 작성자 로그인한 유저 author = request.user
            serializer.save(author=User.objects.get(id=1))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
