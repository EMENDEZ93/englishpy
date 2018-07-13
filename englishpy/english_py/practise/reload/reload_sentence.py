import os

import xlrd
from django.shortcuts import render, get_object_or_404

from ..models.verb.sentence_present import SentencePresent
from ..models.verb.present import Present


def reload_sentence(request, template_name='sentence.html'):
    data = {}
    current_main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(current_main_folder, 'reload/ingles.xlsx')
    excel = xlrd.open_workbook(ruta)
    reading = excel.sheet_by_index(6)

    added_verbs = list()

    print('*******************')
    for row in range(0,reading.nrows-1):
        if not SentencePresent.objects.filter(secondary_id=reading.cell(row,4).value).exists():
            if Present.objects.filter(verb=reading.cell(row,3).value).exists():
                verb = get_object_or_404(Present, verb=reading.cell(row,3).value)
                SentencePresent.objects.create(
                    verb = verb,
                    sentence =reading.cell(row,2).value ,
                    secondary_id =reading.cell(row,4).value ,
                    auxiliary =reading.cell(row,1).value
                )
                added_verbs.append(reading.cell(row,4).value)
                #print(verb)
                #print(reading.cell(row,3).value)
                #print(reading.cell(row,2).value)
                #print(reading.cell(row,4).value)
                #print(reading.cell(row,1).value)
                #print('*******************')



    data['sentences'] = added_verbs

    return render(request,template_name, data)

