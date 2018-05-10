# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Present, PastParticiple, Past, Routine, Topic, Vocabulary, LearnedWord


class PresentAdmin(admin.ModelAdmin):
    list_display = ('verb', 'category',)

admin.site.register(Present, PresentAdmin)


class PastAdmin(admin.ModelAdmin):
    list_display = ('verb', 'present',)

admin.site.register(Past, PastAdmin)


class PastParticipleAdmin(admin.ModelAdmin):
    list_display = ('verb', 'present',)

admin.site.register(PastParticiple, PastParticipleAdmin)


class RoutineAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Routine, RoutineAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'routine')

admin.site.register(Topic, TopicAdmin)


class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('word', 'routine', 'learned',)

admin.site.register(Vocabulary, VocabularyAdmin)


class LearnedWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'topic',)

admin.site.register(LearnedWord, LearnedWordAdmin)
