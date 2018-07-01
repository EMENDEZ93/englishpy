# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SentencePhrasalVerb(models.Model):
    phrasal_verb = models.ForeignKey('PhrasalVerb', verbose_name=_('Present'))
    sentence = models.TextField(_('Sentence'), unique=True)
    secondary_id = models.CharField(_('Secondary Id'),max_length=50)
    auxiliary = models.CharField(_('Auxiliary'),max_length=50)

    def __str__(self):
        return self.sentence