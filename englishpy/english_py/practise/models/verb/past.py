# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


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