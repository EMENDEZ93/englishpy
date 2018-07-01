from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

<<<<<<< HEAD
from ..models.sentence_present import SentencePresent
from ..types import VerbTypes
from ..models.present import Present
from ..models.learned_present import LearnedPresent
=======
from ..models.models import Present, LearnedPresent, SentencePresent
from ..types import VerbTypes
>>>>>>> parent of bf9e46c... splitting models


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


def get_sentence_number(request, present):
    verb = get_object_or_404(Present,verb=present)
    data = {'sentence_number': len(verb.get_all_sentence())}
    return JsonResponse(data)


def get_sentence(request, _id, present):
    sentence = get_object_or_404(SentencePresent,secondary_id='{}{}'.format(present, _id))
    data = {'sentence': sentence.sentence }
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

