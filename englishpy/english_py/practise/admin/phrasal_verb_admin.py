# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from ..models.phrasal_verb.phrasal_verb import PhrasalVerb


class PhrasalVerbAdmin(admin.ModelAdmin):
    list_display = ('phrasal_verb',)

admin.site.register(PhrasalVerb, PhrasalVerbAdmin)
