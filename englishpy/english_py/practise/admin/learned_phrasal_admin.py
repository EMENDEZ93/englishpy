# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ..models.learned.learned_phrasal import LearnedPhrasal


class LearnedPhrasalAdmin(admin.ModelAdmin):
    list_display = ('user', 'phrasal')

admin.site.register(LearnedPhrasal, LearnedPhrasalAdmin)