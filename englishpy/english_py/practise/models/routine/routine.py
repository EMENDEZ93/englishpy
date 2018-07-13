# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Routine(models.Model):
    name = models.CharField(_('Nombre de la rutina'), max_length=255, unique=True)
    user = models.ForeignKey(User, verbose_name=_('Usuario'), null=True, blank=True)

    def __str__(self):
        return self.name
