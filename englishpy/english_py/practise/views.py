# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Verb

def home(request, template_name='practise/review/home.html'):
    ver = Verb()
    return render(request, template_name)