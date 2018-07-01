# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models.models import Present, PastParticiple, Past, Routine, Topic, Vocabulary, LearnedPresent, SentencePresent


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


class LearnedPresentAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'category')

admin.site.register(LearnedPresent, LearnedPresentAdmin)


class SentencePresentAdmin(admin.ModelAdmin):
    list_display = ('verb', 'sentence', 'secondary_id', 'auxiliary')

admin.site.register(SentencePresent, SentencePresentAdmin)