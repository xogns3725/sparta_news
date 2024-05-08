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
from rest_framework import generics
# Create your views here.


class ArticleListView(generics.ListAPIView):  # 페이지 네이션
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

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
