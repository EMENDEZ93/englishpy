# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from ..models.vocabulary.vocabulary import  Vocabulary


class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('word', 'routine', 'learned',)

admin.site.register(Vocabulary, VocabularyAdmin)