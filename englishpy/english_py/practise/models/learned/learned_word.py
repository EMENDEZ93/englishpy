# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import Topic


class LearnedWord(models.Model):
    word = models.CharField(_('Palabra aprendida'), max_length=255, null=True, blank=True)
    topic = models.ForeignKey(Topic, verbose_name=_('Tema'))

    def __str__(self):
        return self.word