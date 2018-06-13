from django.shortcuts import render, get_object_or_404

from ..types import VerbTypes
from .forms import VerbForm
from ..models import Present, Learned_Present
from django.http import JsonResponse
from random import randint
from django.db.models import Q
import os
from django.conf import settings


def home(request, template_name='practise/review/home.html'):
    data={}

    print(settings.MEDIA_URL)

    data['audio'] = 'media/english/verb/present/work.mp3'
    return render(request, template_name, data)


def next_verb(request):
    data = {}
    learned_word(request)
    verb = get_object_or_404(Present,verb=exclude_words(request))
    data = {
        'present': verb.present_object(),
        'past': verb.past(),
        'past_participle':verb.past_participle()
    }
    return JsonResponse(data)


def learned_word(request):
    if request.user.is_authenticated:
        if request.GET['learned_word'] != '':
            if not Learned_Present.objects.filter(user=request.user,verb=request.GET['learned_word']):
                Learned_Present.objects.create(
                    user=request.user,
                    verb=request.GET['learned_word'],
                    category=VerbTypes.REGULAR
                )

    return ''


def exclude_words(request):
    learned_present_verb = Learned_Present.objects.filter(user=request.user, category=VerbTypes.REGULAR).values_list('verb', flat=True)
    id_verb = Present.objects.all().exclude(verb__in=learned_present_verb).values_list('verb', flat=True)[:1]
    return id_verb[0]
