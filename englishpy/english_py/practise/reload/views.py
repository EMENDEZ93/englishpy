import os

import xlrd
from django.shortcuts import render
from ..models import Verb, OtherTime
from ..types import TimesTypes

def reload(request, template_name='xlsx.html'):
    data = {}
    current_main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(current_main_folder, 'reload/ingles.xlsx')
    excel = xlrd.open_workbook(ruta)
    reading = excel.sheet_by_index(5)

    verbos = list()
    col = 0
    for row in range(0,reading.nrows-1):
            Verb.objects.create(present=reading.cell(row,col).value)

    data['verbos'] = Verb.objects.all()

    return render(request,template_name, data)


def reload_other_time(request, template_name='other_time.html'):
    current_main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(current_main_folder, 'reload/ingles.xlsx')
    excel = xlrd.open_workbook(ruta)
    reading = excel.sheet_by_index(5)

    verbs = Verb.objects.all()
    col = 1
    for row in range(0,reading.nrows-1):
            print( str(verbs[row]) +' : ' + str(reading.cell(row,col).value))
            OtherTime.objects.create(verb=reading.cell(row,col).value,time=TimesTypes.PAST,present=verbs[row])
            OtherTime.objects.create(verb=reading.cell(row,2).value,time=TimesTypes.PAST_PARTICIPLE,present=verbs[row])



    return render(request,template_name,)



def delete_all_other(request, template_name='all_delete.html'):
    OtherTime.objects.all().delete()
    return render(request, template_name)



def delete_all_verb(request, template_name='all_delete.html'):
    Verb.objects.all().delete()
    return render(request, template_name)
