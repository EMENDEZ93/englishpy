# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import models
from ..types import VerbTypes, TimesTypes, TopicTypes


class Past(models.Model):
    verb = models.CharField(_('Past'), max_length=255, unique=True)
    present = models.ForeignKey('Present', verbose_name=_('Present'))

    def __str__(self):
        return self.verb

    def past_object(self):
        data = {
            'verb':self.verb,
            'audio':'media/english/verb/past/{}.mp3'.format(self.verb)
        }
        return data


class PastParticiple(models.Model):
    verb = models.CharField(_('Past participle'), max_length=255, unique=True)
    present = models.ForeignKey('Present', verbose_name=_('Present'))

    def __str__(self):
        return self.verb

    def past_participle_object(self):
        data = {
            'verb':self.verb,
            'audio':'media/english/verb/past_participle/{}.mp3'.format(self.verb)
        }
        return data


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


class Vocabulary(models.Model):
    word = models.CharField(_('Palabra'), max_length=255)
    routine = models.ForeignKey(Topic, verbose_name=_('Tema'))
    learned = models.BooleanField(_('¿Aprendido?'), default=False)

    def __str__(self):
        return self.word


class LearnedPresent(models.Model):
    user = models.ForeignKey(User, verbose_name=_('usuario'))
    verb = models.CharField(_('Present'), max_length=255, unique=True)
    category = models.CharField(_('Type'),max_length=255, default=VerbTypes.REGULAR)

    def __str__(self):
        return self.verb


class SentencePresent(models.Model):
    verb = models.ForeignKey('Present', verbose_name=_('Present'))
    sentence = models.TextField(_('Sentence'), unique=True)
    secondary_id = models.CharField(_('Secondary Id'),max_length=50)
    auxiliary = models.CharField(_('Auxiliary'),max_length=50)

    def __str__(self):
        return self.sentence
