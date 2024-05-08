from .models import Article, Comments
from rest_framework import serializers

class CommentsSerializer(serializers.ModelSerializer):
    # likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ['content',]
        # read_only_fields = ("article",)
    
    # def get_likes_count(self, obj):
    #     return obj.comment_likes.count()

class ArticleSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['title', 'content', 'url', 'likes_count',]
    
    def get_likes_count(self, obj):
        return obj.article_likes.count()
        
class ArticleDetailSerializer(ArticleSerializer):
    #추후 코멘트 추가해야함
    pass
