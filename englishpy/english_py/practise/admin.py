# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Verb, OtherTime


class VerbAdmin(admin.ModelAdmin):
    list_display = ('present', 'category',)

admin.site.register(Verb, VerbAdmin)


class OtherTimeAdmin(admin.ModelAdmin):
    list_display = ('verb', 'time', 'present',)

admin.site.register(OtherTime, OtherTimeAdmin)
