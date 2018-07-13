# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import models
from ..types import VerbTypes, TimesTypes, TopicTypes


class Topic(models.Model):
    name = models.CharField(_('Tema'), max_length=512, choices=TopicTypes.TYPES, default=TopicTypes.DEFAULT, unique=True)
    routine = models.ForeignKey('Routine', verbose_name=_('Rutina'))
    repetitions = models.IntegerField(_('Repeticiones'), default=5)

    def __str__(self):
        return self.name