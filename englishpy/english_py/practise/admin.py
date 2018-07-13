# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models.phrasal_verb.learned_phrasal import LearnedPhrasal
from .models.topic.topic import Topic
from .models.phrasal_verb.phrasal_verb import PhrasalVerb
from .models.phrasal_verb.sentence_phrasal_verb import SentencePhrasalVerb
from .models.verb.sentence_present import  SentencePresent
from .models.learned.learned_present import LearnedPresent
from .models.vocabulary.vocabulary import  Vocabulary


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'routine', 'repetitions')

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


class PhrasalVerbAdmin(admin.ModelAdmin):
    list_display = ('phrasal_verb',)

admin.site.register(PhrasalVerb, PhrasalVerbAdmin)


class SentencePhrasalVerbAdmin(admin.ModelAdmin):
    list_display = ('phrasal_verb', 'sentence', 'secondary_id', 'auxiliary',)

admin.site.register(SentencePhrasalVerb, SentencePhrasalVerbAdmin)


class LearnedPhrasalbAdmin(admin.ModelAdmin):
    list_display = ('user', 'phrasal')

admin.site.register(LearnedPhrasal, LearnedPhrasalbAdmin)
