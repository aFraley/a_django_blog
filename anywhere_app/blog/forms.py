from django.forms import ModelForm

from .models import Topic, Comment


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'body']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Comment'
        }
