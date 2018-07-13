# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from ...types import VerbTypes


class LearnedPresent(models.Model):
    user = models.ForeignKey(User, verbose_name=_('usuario'))
    verb = models.CharField(_('Present'), max_length=255, unique=True)
    category = models.CharField(_('Type'),max_length=255, default=VerbTypes.REGULAR)

    def __str__(self):
        return self.verb