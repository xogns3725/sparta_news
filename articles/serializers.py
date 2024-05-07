from .models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'url', 'likes_count',]
    
    def get_likes_count(self, obj):
        return obj.article_likes.count()
        
class ArticleDetailSerializer(ArticleSerializer):
    # comment 추가해야합니다.
    pass
        