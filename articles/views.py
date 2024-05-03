from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.core.cache import cache
from .models import Article
from .serializers import ArticleSerializer
from accounts.models import User
# Create your views here.


class ArticleListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):  # article 리스트
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):  # 게시글 작성
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        user = request.user.id
        u_user = article.author.id
        print(user, u_user)
        if user == u_user:
            print("일치")
            article.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("작성자와 삭제자 id 불일치", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        user = request.user.id
        up_user = article.author.id
        print(user, up_user)
        if user == up_user:
            serializer = ArticleSerializer(
                article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response("작성자가 아닌디 왜 수정할라그려", status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        user = request.user
        if user in article.article_likes.all():
            article.article_likes.remove(user)
            article.save()
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            article.article_likes.add(user)
            article.save()
            return Response("좋아요 성공", status=status.HTTP_201_CREATED)
