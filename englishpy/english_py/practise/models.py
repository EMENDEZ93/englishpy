# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import models
from types import VerbTypes, TimesTypes


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
    verb = models.CharField(_('past'), max_length=255, unique=True)
    present = models.ForeignKey(Present, verbose_name=_('Present'))

    def __str__(self):
        return self.verb


class PastParticiple(models.Model):
    verb = models.CharField(_('past_participle'), max_length=255, unique=True)
    present = models.ForeignKey(Present, verbose_name=_('Present'))

    def __str__(self):
        return self.verb
