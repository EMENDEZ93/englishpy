import os
import xlrd
from django.shortcuts import render

from ..models import Present


def reload_phrasal(request, template_name='xlsx.html'):
    data = {}
    current_main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(current_main_folder, 'reload/ingles.xlsx')
    excel = xlrd.open_workbook(ruta)
    reading = excel.sheet_by_index(6)

    added_verbs = list()

    for row in range(0,reading.nrows-1):
        if Present.objects.filter(verb=reading.cell(row,0).value).exists():
        #    Present.objects.create(verb=reading.cell(row,0).value)
            added_verbs.append(reading.cell(row,0).value)
            print(reading.cell(row,2).value)
        #print(reading.cell(row,2).value)
    data['verbos'] = added_verbs

    return render(request,template_name, data)

