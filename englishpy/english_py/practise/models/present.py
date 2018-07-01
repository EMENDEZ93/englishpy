# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .mo import Past, PastParticiple, SentencePresent
from ..types import VerbTypes


class Present(models.Model):
    verb = models.CharField(_('Present'), max_length=255, unique=True)
    category = models.CharField(_('Type'),max_length=255, default=VerbTypes.REGULAR)

    def __str__(self):
        return self.verb

    def past(self):
        past = Past.objects.get(present=self)
        return past.past_object()

    def past_participle(self):
        past_participle = PastParticiple.objects.get(present=self)
        return past_participle.past_participle_object()

    def present_object(self):
        data = {
            'verb':self.verb,
            'audio':'media/english/verb/present/{}.mp3'.format(self.verb),
            'category':self.category,
        }
        return data

    def get_all_sentence(self):
        #return SentencePresent.objects.filter(verb=self)
        return SentencePresent.objects.filter(verb=self).values_list('sentence', flat=True)