# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .routine import Routine
from ..types import VerbTypes, TimesTypes, TopicTypes


class Vocabulary(models.Model):
    word = models.CharField(_('Palabra'), max_length=255)
    routine = models.ForeignKey('Topic', verbose_name=_('Tema'))
    learned = models.BooleanField(_('¿Aprendido?'), default=False)

    def __str__(self):
        return self.word