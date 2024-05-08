from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, ArticleDetailSerializer
from rest_framework import generics
# Create your views here.


class ArticleListView(generics.ListCreateAPIView):  # 페이지 네이션
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):  # 게시글 작성
        author = request.user
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def delete(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user.id
        u_user = article.author.id
        if user == u_user:
            article.delete()
            return Response("삭제완료", status=status.HTTP_200_OK)
        else:
            return Response("작성자와 삭제자 id 불일치", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user.id
        up_user = article.author.id
        if user == up_user:
            serializer = ArticleSerializer(
                article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response("작성자가 아닌디 왜 수정할라그려", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user
        if user in article.article_likes.all():
            article.article_likes.remove(user)
            article.save()
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            article.article_likes.add(user)
            article.save()
            return Response("좋아요 성공", status=status.HTTP_201_CREATED)

class CommentListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comment_article.all()    
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def put(self, request, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.author:
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete(self, request, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.author:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)   
        
    def post(self, request, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        user = request.user
        if user in comment.comment_likes.all():
            comment.comment_likes.remove(user)
            comment.save()
            return Response("좋아요 취소", status=status.HTTP_200_OK)
        else:
            comment.comment_likes.add(user)
            comment.save()
            return Response("좋아요 성공", status=status.HTTP_201_CREATED)