from django.shortcuts import render, get_object_or_404
from .forms import VerbForm
from ..models import Present
from django.http import JsonResponse
from random import randint
import os
from django.conf import settings


def home(request, template_name='practise/review/home.html'):
    data = {}
    data['verb'] = Present.objects.all()[:5]
    data['form'] = VerbForm()

    print(settings.MEDIA_URL)

    data['audio'] = 'media/english/verb/present/work.mp3'

    return render(request, template_name, data)


def next_verb(request):

    data = {}
    next_id = int()

    id_used_list = []
    for i in request.GET['hi']:
        if not i == ',':
            if int(i) or int(i) == 0:
                id_used_list.append(int(i))


    id_prefer_user =[ i.id for i in Present.objects.all()[:1]]


    if len(id_used_list) != len(id_prefer_user):
        next_id = randint(0, len(id_prefer_user) - 1)
        while (next_id in id_used_list):
            next_id = randint(0, len(id_prefer_user)-1)
        data['id'] = next_id
        data['finished_routine'] = False
    else:
        data['finished_routine'] = True

    verb = get_object_or_404(Present,pk=id_prefer_user[next_id])
    data = {
        'present': verb.present_object(),
        'past': verb.past(),
        'past_participle':verb.past_participle()
    }

    return JsonResponse(data)




