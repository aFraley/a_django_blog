from django.conf.urls import url, include
from django.contrib.auth.views import login

from . import views


urlpatterns = [
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^registration/$', views.Registration.as_view(), name='registration')
]
