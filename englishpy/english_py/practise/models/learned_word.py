# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .routine import Routine
from ..types import VerbTypes, TimesTypes, TopicTypes


class LearnedWord(models.Model):
    word = models.CharField(_('Palabra aprendida'), max_length=255, null=True, blank=True)
    topic = models.ForeignKey('Topic', verbose_name=_('Tema'))

    def __str__(self):
        return self.word