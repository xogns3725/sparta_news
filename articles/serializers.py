from .models import Article, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['content', 'likes_count']
        read_only_fields = ("article",)  # 외래키 수정 못하게

    def get_likes_count(self, obj):
        return obj.comment_likes.count()


class ArticleSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('title', 'content', 'url',
                  'author', 'likes_count', 'comments')

    def get_likes_count(self, obj):
        return obj.article_likes.count()


class ArticleDetailSerializer(ArticleSerializer):
    comments = CommentSerializer(many=True, read_only=True)
