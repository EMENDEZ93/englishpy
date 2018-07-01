# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-01 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practise', '0012_delete_presente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=255, unique=True, verbose_name='Present')),
                ('category', models.CharField(default='Regular', max_length=255, verbose_name='Type')),
            ],
        ),
    ]
