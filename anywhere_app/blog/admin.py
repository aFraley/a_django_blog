from django.contrib import admin

from .models import Topic, Comment


class TopicAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment)
