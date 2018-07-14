# -*- coding: utf-8 -*-
from django.shortcuts import render

def base(request, template_name='practise/base.html'):
    return render(request, template_name)