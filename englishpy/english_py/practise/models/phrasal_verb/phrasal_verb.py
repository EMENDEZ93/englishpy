# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ...types import VerbTypes


class PhrasalVerb(models.Model):
    phrasal_verb = models.CharField(_('Phrasal Verb'), max_length=255, unique=True)


    def __str__(self):
        return self.phrasal_verb
