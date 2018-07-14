# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
#from ..models.routine.routine import Routine
from ..models import Routine

class RoutineAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Routine, RoutineAdmin)
