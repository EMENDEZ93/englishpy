from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from ..types import TopicTypes
from ..models.models import Topic
from ..models.phrasal_verb.sentence_phrasal_verb import SentencePhrasalVerb
from ..models.phrasal_verb.learned_phrasal import LearnedPhrasal
from ..models.phrasal_verb.phrasal_verb import PhrasalVerb


def learning_phrasal(request, template_name='practise/review/phrasal/learning.html'):
    data={}
    topic = Topic.objects.get(name=TopicTypes.LEARNED_PHRASAL)
    data['repetitions']= topic.repetitions
    return render(request, template_name, data)


def next_phrasal(request):
    phrasal = get_object_or_404(PhrasalVerb,phrasal_verb=exclude_words(request))
    data = {'phrasal': phrasal.phrasal_verb }
    return JsonResponse(data)


def exclude_words(request):
    learned_phrasal = LearnedPhrasal.objects.filter(user=request.user).values_list('phrasal', flat=True)
    id_phrasal = PhrasalVerb.objects.all().exclude(phrasal_verb__in=learned_phrasal).values_list('phrasal_verb', flat=True)[:1]
    return id_phrasal[0]


def get_sentence_phrasal_number(request, phrasal):
    phrasal_verb = get_object_or_404(PhrasalVerb,phrasal_verb=phrasal)
    data = {'sentence_number': len(SentencePhrasalVerb.objects.filter(phrasal_verb=phrasal_verb).values_list('sentence', flat=True))}
    return JsonResponse(data)


def get_sentence_phrasal(request, phrasal_id):
    sentence = get_object_or_404(SentencePhrasalVerb,secondary_id='{}'.format(phrasal_id))
    data = {'sentence': sentence.sentence }
    return JsonResponse(data)


def learned_phrasal(request, learned_phrasal):
    data={}
    if request.user.is_authenticated:
        if learned_phrasal != '':
            if not LearnedPhrasal.objects.filter(user=request.user,phrasal=learned_phrasal):
                LearnedPhrasal.objects.create(
                    user=request.user,
                    phrasal=learned_phrasal
                )

    return JsonResponse(data)
