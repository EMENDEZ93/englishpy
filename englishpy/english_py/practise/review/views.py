from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from ..types import TopicTypes
from .forms import VerbForm
from ..models import Present, LearnedWord, Topic
from django.http import JsonResponse
from random import randint
from django.db.models import Q
import os
from django.conf import settings


def home(request, template_name='practise/review/home.html'):
    data={}
    data['verb'] = Present.objects.filter(
        ~Q(verb__in=LearnedWord.objects.filter(topic__routine__user=request.user)
        .values_list('word', flat=True))).first()

    data['form'] = VerbForm()
    data['audio'] = 'media/english/verb/present/work.mp3'
    return render(request, template_name, data)


def next_verb(request):
    verb = Present.objects.filter(~Q(verb__in=LearnedWord.objects.filter(
        topic__routine__user=request.user)
        .values_list('word', flat=True))
        ).first()

    data = {
        'present': verb.present_object(),
        'past': verb.past(),
        'past_participle':verb.past_participle()
    }
    return JsonResponse(data)


@csrf_exempt
def register_learned_word(request):
    data = {}
    if request.user.is_authenticated():
        LearnedWord.objects.create(
            word=request.POST['learned_word'],
            topic=Topic.objects.get(routine__user=request.user, name=TopicTypes.VERBS))
    return JsonResponse(data)
