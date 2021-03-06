from django.shortcuts import render

from ..models.learned.learned_present import LearnedPresent


def review(request, template_name='practise/review/review.html'):
    data={}
    data['learned_present'] = get_all_learned_present(request)
    return render(request, template_name, data)


def get_all_learned_present(request):
    if request.user.is_authenticated:
        return LearnedPresent.objects.filter(user=request.user).values_list('verb', flat=True)








