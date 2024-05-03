from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import Article
from .serializers import ArticleSrializer
# Create your views here.


class ArticleListAPIView(APIView):
    def get(self, request):#article 리스트
        articles = Article.objects.all()
        serializer = ArticleSrializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSrializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author = "adim") #author = request.user
