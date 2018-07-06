from django.shortcuts import render


def learning_phrasal(request, template_name='practise/review/phrasal/learning.html'):
    data={}
    return render(request, template_name, data)


#def next_phrasal(request):
#    verb = get_object_or_404(Present,verb=exclude_words(request))
#    data = {'present': verb.present_object()}
#    return JsonResponse(data)
#
#
#def exclude_words(request):
#    learned_present_verb = LearnedPresent.objects.filter(user=request.user, category=VerbTypes.REGULAR).values_list('verb', flat=True)
#    id_verb = Present.objects.all().exclude(verb__in=learned_present_verb).values_list('verb', flat=True)[:1]
#    return id_verb[0]
