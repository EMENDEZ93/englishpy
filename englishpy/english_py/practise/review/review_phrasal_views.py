from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from ..models.phrasal_verb.learned_phrasal import LearnedPhrasal
from ..models.phrasal_verb.phrasal_verb import PhrasalVerb


def learning_phrasal(request, template_name='practise/review/phrasal/learning.html'):
    data={}
    return render(request, template_name, data)


def next_phrasal(request):
    print('*********************************')
    phrasal = get_object_or_404(PhrasalVerb,phrasal_verb=exclude_words(request))
    data = {'phrasal': phrasal.phrasal_verb }
    print(data)
    return JsonResponse(data)


def exclude_words(request):
    learned_phrasal = LearnedPhrasal.objects.filter(user=request.user).values_list('phrasal', flat=True)
    id_phrasal = PhrasalVerb.objects.all().exclude(phrasal_verb__in=learned_phrasal).values_list('phrasal_verb', flat=True)[:1]
    return id_phrasal[0]
