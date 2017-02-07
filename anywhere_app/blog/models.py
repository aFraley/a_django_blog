from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='comment_author', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('body', 'author')

    def __str__(self):
        return self.body
