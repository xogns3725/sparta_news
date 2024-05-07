from .models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    article_likes = serializers.IntegerField(source="article_likes.count", read_only=True)
    class Meta:
        model = Article
        fields = ['title', 'content', 'url',]
        
class ArticleDetailSerializer(ArticleSerializer):
    #추후 코멘트 추가해야함
    pass