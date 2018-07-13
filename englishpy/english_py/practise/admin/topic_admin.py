# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from ..models.topic.topic import Topic

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'routine', 'repetitions')

admin.site.register(Topic, TopicAdmin)
