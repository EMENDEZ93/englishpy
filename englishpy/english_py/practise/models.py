# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import models
from types import VerbTypes, TimesTypes, TopicTypes


class Present(models.Model):
    verb = models.CharField(_('Present'), max_length=255, unique=True)
    category = models.CharField(_('Type'),max_length=255, default=VerbTypes.REGULAR)

    def __str__(self):
        return self.verb

    def past(self):
        past = Past.objects.get(present=self)
        return str(past)

    def past_participle(self):
        past_participle = PastParticiple.objects.get(present=self)
        return str(past_participle.verb)


class Past(models.Model):
    verb = models.CharField(_('Past'), max_length=255, unique=True)
    present = models.ForeignKey(Present, verbose_name=_('Present'))

    def __str__(self):
        return self.verb


class PastParticiple(models.Model):
    verb = models.CharField(_('Past participle'), max_length=255, unique=True)
    present = models.ForeignKey(Present, verbose_name=_('Present'))

    def __str__(self):
        return self.verb


class Routine(models.Model):
    name = models.CharField(_('Nombre de la rutina'), max_length=255, unique=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(_('Tema'), max_length=512, choices=TopicTypes.TYPES, default=TopicTypes.DEFAULT, unique=True)
    routine = models.ForeignKey(Routine, verbose_name=_('Rutina'))

    def __str__(self):
        return self.name


class Vocabulary(models.Model):
    word = models.CharField(_('Palabra'), max_length=255)
    routine = models.ForeignKey(Topic, verbose_name=_('Tema'))
    learned = models.BooleanField(_('¿Aprendido?'), default=False)

    def __str__(self):
        return self.word

