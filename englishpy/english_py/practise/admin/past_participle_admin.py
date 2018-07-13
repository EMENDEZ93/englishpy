# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from ..models.verb.past_participle import PastParticiple


class PastParticipleAdmin(admin.ModelAdmin):
    list_display = ('verb', 'present',)

admin.site.register(PastParticiple, PastParticipleAdmin)