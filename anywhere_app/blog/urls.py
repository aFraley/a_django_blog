from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'create/$', login_required(views.TopicCreate.as_view()), name='create'),
    url(r'topics/(?P<topic_id>\d+)/$', login_required(views.TopicDetail.as_view()), name='topic'),
    url(r'comments/(?P<topic_id>\d+)/$', login_required(views.Comments.as_view()), name='comments'),
    url(r'$', login_required(views.TopicsView.as_view()), name='topics')
]
