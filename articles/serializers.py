from .models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'url',
                  'created_at', 'updated_at', 'author']
        read_only_fields = ('author',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'url',
                  'created_at', 'updated_at', 'author']
        read_only_fields = ('author',)
