# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.db import models
from types import VerbTypes, TimesTypes


class Verb(models.Model):
    present = models.CharField(_('Present'), max_length=255)
    category = models.CharField(_('Type'),max_length=255, choices=VerbTypes.TYPES, default=VerbTypes.REGULAR)

    def __str__(self):
        return self.present

    def past(self):
        past = OtherTime.objects.get(present__present=self.present, time=TimesTypes.PAST)
        return past

class OtherTime(models.Model):
    verb = models.CharField(_('Present'), max_length=255)
    time = models.CharField(_('Time'),max_length=255, choices=TimesTypes.TYPES, default=TimesTypes.PAST)
    present = models.ForeignKey(Verb, verbose_name=_('Present'))

    def __str__(self):
        return self.verb