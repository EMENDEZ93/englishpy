# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models


class SentencePresent(models.Model):
    verb = models.ForeignKey('Present', verbose_name=_('Present'))
    sentence = models.TextField(_('Sentence'), unique=True)
    secondary_id = models.CharField(_('Secondary Id'),max_length=50)
    auxiliary = models.CharField(_('Auxiliary'),max_length=50)

    def __str__(self):
        return self.sentence
