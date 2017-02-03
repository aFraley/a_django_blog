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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
