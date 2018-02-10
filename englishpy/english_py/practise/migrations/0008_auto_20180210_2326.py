# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-10 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practise', '0007_auto_20180210_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(choices=[(b'VERBS', b'VERBS'), (b'--------------------', b'--------------------')], default=b'--------------------', max_length=512, unique=True, verbose_name='Tema'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practise.Routine', verbose_name='Rutina'),
        ),
    ]
