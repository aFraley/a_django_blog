from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'create/$', login_required(views.TopicCreate.as_view()), name='create'),
    url(r'topics/$', login_required(views.TopicsView.as_view()), name='topics'),
    url(r'topics/(?P<topic_id>\d+)$', login_required(views.TopicDetail.as_view()), name='topic')
]