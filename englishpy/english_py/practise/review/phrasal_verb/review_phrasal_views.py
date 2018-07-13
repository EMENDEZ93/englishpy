from django.shortcuts import render

from ...models.learned.learned_phrasal import LearnedPhrasal


def review_phrasal(request, template_name='practise/review/phrasal/review.html'):
    data={}
    data['learned_phrasal'] = get_all_learned_phrasal(request)
    return render(request, template_name, data)


def get_all_learned_phrasal(request):
    if request.user.is_authenticated:
        return LearnedPhrasal.objects.filter(user=request.user).values_list('phrasal', flat=True)
