# -*- coding: utf-8 -*-
from django.shortcuts import render

def searcher(request, template_name='searcher.html'):
    return render(request, template_name)