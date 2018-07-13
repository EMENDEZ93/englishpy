# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import models
from ..types import VerbTypes, TimesTypes, TopicTypes


class Routine(models.Model):
    name = models.CharField(_('Nombre de la rutina'), max_length=255, unique=True)
    user = models.ForeignKey(User, verbose_name=_('Usuario'), null=True, blank=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(_('Tema'), max_length=512, choices=TopicTypes.TYPES, default=TopicTypes.DEFAULT, unique=True)
    routine = models.ForeignKey(Routine, verbose_name=_('Rutina'))
    repetitions = models.IntegerField(_('Repeticiones'), default=5)

    def __str__(self):
        return self.name


class LearnedWord(models.Model):
    word = models.CharField(_('Palabra aprendida'), max_length=255, null=True, blank=True)
    topic = models.ForeignKey(Topic, verbose_name=_('Tema'))

    def __str__(self):
        return self.word