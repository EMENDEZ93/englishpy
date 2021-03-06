# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ...types import VerbTypes
from ..verb.sentence_present import  SentencePresent
from ..verb.past import Past
from ..verb.past_participle import PastParticiple


class Present(models.Model):
    verb = models.CharField(_('Present'), max_length=255, unique=True)
    category = models.CharField(_('Type'),max_length=255, default=VerbTypes.REGULAR)

    def __str__(self):
        return self.verb

    def past(self):
        past = Past.objects.get(present=self)
        return past.past_object()

    def past_participle(self):
        past_participle = PastParticiple.objects.get(present=self)
        return past_participle.past_participle_object()

    def present_object(self):
        data = {
            'verb':self.verb,
            'audio':'media/english/verb/present/{}.mp3'.format(self.verb),
            'category':self.category,
        }
        return data

    def get_all_sentence(self):
        #return SentencePresent.objects.filter(verb=self)
        return SentencePresent.objects.filter(verb=self).values_list('sentence', flat=True)