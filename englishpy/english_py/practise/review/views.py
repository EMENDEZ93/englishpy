from django.shortcuts import render, get_object_or_404
from .forms import VerbForm
from ..models import Present
from django.http import JsonResponse
from random import randint
import os

def home(request, template_name='practise/review/home.html'):
    data = {}
    data['verb'] = Present.objects.all()
    data['form'] = VerbForm()

    current_main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(current_main_folder, 'review/translate_tts.mp3')

    data['audio'] = ruta

    return render(request, template_name, data)


def next_verb(request):

    data = {}
    next_id = int()

    id_used_list = []
    for i in request.GET['hi']:
        if not i == ',':
            if int(i) or int(i) == 0:
                id_used_list.append(int(i))


    id_prefer_user =[ i.id for i in Present.objects.all()]


    if len(id_used_list) != len(id_prefer_user):
        next_id = randint(0, len(id_prefer_user) - 1)
        while (next_id in id_used_list):
            next_id = randint(0, len(id_prefer_user)-1)
        data['id'] = next_id
        data['finished_routine'] = False
    else:
        data['finished_routine'] = True

    verb = get_object_or_404(Present,pk=id_prefer_user[next_id])

    data['present'] = str(verb.verb)
    data['past'] = str(verb.past())
    data['past_participle'] = str(verb.past_participle())

    print('**************************************')
    print(verb.past())


    return JsonResponse(data)




