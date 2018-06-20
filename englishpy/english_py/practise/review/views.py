from django.shortcuts import render, get_object_or_404

from ..types import VerbTypes
from .forms import VerbForm
from ..models import Present, LearnedPresent, SentencePresent
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
    verb = get_object_or_404(Present,verb=exclude_words(request))
    data = {'present': verb.present_object()}
    return JsonResponse(data)


def get_past(request, present):
    verb = get_object_or_404(Present,verb=present)
    data = {'past': verb.past()}
    return JsonResponse(data)


def get_past_participle(request, present):
    verb = get_object_or_404(Present,verb=present)
    data = {'past_participle': verb.past_participle()}
    return JsonResponse(data)


def learned_word(request, learned_word):
    data={}
    if request.user.is_authenticated:
        if learned_word != '':
            if not LearnedPresent.objects.filter(user=request.user,verb=learned_word):
                LearnedPresent.objects.create(
                    user=request.user,
                    verb=learned_word,
                    category=VerbTypes.REGULAR
                )

    return JsonResponse(data)


def exclude_words(request):
    learned_present_verb = LearnedPresent.objects.filter(user=request.user, category=VerbTypes.REGULAR).values_list('verb', flat=True)
    id_verb = Present.objects.all().exclude(verb__in=learned_present_verb).values_list('verb', flat=True)[:1]
    return id_verb[0]


def next_sentence(request):
    if int(request.GET['number_sentence_pivot']) <= int(request.GET['number_sentence']):
        sentence = SentencePresent.objects.get(secondary_id=request.GET['present'] + request.GET['number_sentence_pivot'])
        if sentence:
            data ={'sentence': sentence.sentence}

    return JsonResponse(data)

