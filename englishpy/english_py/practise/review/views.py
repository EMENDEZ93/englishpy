from django.shortcuts import render


def home(request, template_name='practise/review/home.html'):
    return render(request, template_name)