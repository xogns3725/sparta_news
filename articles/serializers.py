from .models import Article
from rest_framework import serializers


class ArticleSrializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'url', 'created_at', 'updated_at']
