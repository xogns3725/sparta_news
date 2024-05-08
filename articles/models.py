from django.db import models
from accounts.models import User


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    url = models.URLField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='article_author')
    article_likes = models.ManyToManyField(User,related_name='article_likes',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_author')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment_article')
    created_at = models.DateTimeField(auto_now_add=True)
    comment_likes = models.ManyToManyField(User,related_name='comment_likes')
