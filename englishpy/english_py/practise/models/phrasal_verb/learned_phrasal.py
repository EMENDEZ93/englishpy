# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class LearnedPhrasal(models.Model):
    user = models.ForeignKey(User, verbose_name=_('usuario'))
    phrasal = models.CharField(_('phrasal'), max_length=255, unique=True)

    def __str__(self):
        return self.verb
