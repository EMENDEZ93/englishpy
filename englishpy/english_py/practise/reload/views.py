import os

import xlrd
from django.shortcuts import render

from ..models.mo import Past, PastParticiple
from ..models.present import Present


def reload(request, template_name='xlsx.html'):
    data = {}
    current_main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(current_main_folder, 'reload/ingles.xlsx')
    excel = xlrd.open_workbook(ruta)
    reading = excel.sheet_by_index(5)

    added_verbs = list()

    for row in range(0,reading.nrows-1):
        if not Present.objects.filter(verb=reading.cell(row,0).value).exists():
            Present.objects.create(verb=reading.cell(row,0).value)
            added_verbs.append(reading.cell(row,0).value)

    data['verbos'] = added_verbs

    return render(request,template_name, data)


def reload_other_time(request, template_name='other_time.html'):
    data = {}
    current_main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(current_main_folder, 'reload/ingles.xlsx')
    excel = xlrd.open_workbook(ruta)
    reading = excel.sheet_by_index(5)

    verbs = Present.objects.all()
    for row in range(0,reading.nrows-1):
        if not Past.objects.filter(verb=reading.cell(row,1).value).exists():
            Past.objects.create(verb=reading.cell(row,1).value, present=verbs[row])
        if not PastParticiple.objects.filter(verb=reading.cell(row,2).value).exists():
            PastParticiple.objects.create(verb=reading.cell(row,2).value,present=verbs[row])

    return render(request,template_name,)



def delete_all_other(request, template_name='all_delete.html'):
    PastParticiple.objects.all().delete()
    Past.objects.all().delete()
    return render(request, template_name)



def delete_all_verb(request, template_name='all_delete.html'):
    Present.objects.all().delete()
    return render(request, template_name)
