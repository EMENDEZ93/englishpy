import os

import xlrd
from django.shortcuts import render

from ..models import PhrasalVerb
from ..models import SentencePhrasalVerb
from ..models.models import Present


def reload_phrasal(request, template_name='xlsx.html'):
    data = {}
    current_main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(current_main_folder, 'reload/ingles.xlsx')
    excel = xlrd.open_workbook(ruta)
    reading = excel.sheet_by_index(2)

    added_verbs = list()

    for row in range(0,reading.nrows-1):
        if not reading.cell(row,0).value == '':
            if not PhrasalVerb.objects.filter(phrasal_verb=reading.cell(row,0).value).exists():
                PhrasalVerb.objects.create(phrasal_verb=reading.cell(row,0).value)
                added_verbs.append(reading.cell(row,0).value)
                print(reading.cell(row,0).value)
    data['verbos'] = added_verbs

    for row in range(0,reading.nrows-1):
        if not reading.cell(row,3).value == '':
            if not SentencePhrasalVerb.objects.filter(secondary_id=reading.cell(row,4).value).exists():
                print(reading.cell(row, 3))
                if PhrasalVerb.objects.filter(phrasal_verb=reading.cell(row, 3).value).exists():
                    SentencePhrasalVerb.objects.create(
                        phrasal_verb =PhrasalVerb.objects.get(phrasal_verb=reading.cell(row, 3).value),
                        sentence =reading.cell(row, 2).value,
                        secondary_id =reading.cell(row,4).value,
                        auxiliary =reading.cell(row, 1).value
                    )


    return render(request,template_name, data)

