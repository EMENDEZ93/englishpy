# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-13 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practise', '0021_learnedphrasal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learnedword',
            name='topic',
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(choices=[('VERBS', 'VERBS'), ('--------------------', '--------------------'), ('LEARNED WORD', 'LEARNED WORD'), ('VOCABULARY', 'VOCABULARY'), ('LEARNED PRESENT', 'LEARNED PRESENT'), ('LEARNED PHRASAL', 'LEARNED PHRASAL')], default='--------------------', max_length=512, unique=True, verbose_name='Tema'),
        ),
        migrations.DeleteModel(
            name='LearnedWord',
        ),
    ]