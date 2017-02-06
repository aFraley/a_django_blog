from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView

from .forms import TopicForm, CommentForm
from .models import Topic, Comment


class TopicsView(ListView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicsView, self).get_context_data(**kwargs)
        context['updated_at'] = timezone.now()
        return context


class Index(View):
    template_name = 'blog/topic_list.html'

    def get(self, request):
        return render(request, self.template_name)


class TopicCreate(View):
    form_class = TopicForm
    template_name = 'blog/create_topic.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('blog:topics')
        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})


class TopicDetail(View):
    template_name = 'blog/topic_detail.html'
    form_class = CommentForm
    topic_model = Topic
    comment_model = Comment

    def get(self, request, topic_id):
        form = self.form_class
        topic = Topic.objects.get(id=topic_id)
        comments = topic.comment_set.order_by('-updated_at')
        context = {
            'topic': topic,
            'comments': comments,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, topic_id):
        form = self.form_class(request.POST)
        topic = self.topic_model.objects.get(id=topic_id)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.topic = topic
            new_comment.save()
            return redirect('blog:topic', topic_id)
        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def delete(self, request, topic_id):
        comment = self.comment_model.objects.get(id=topic_id)
        comment.delete()
        return redirect('blog:topic', topic_id)
