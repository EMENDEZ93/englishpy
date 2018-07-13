# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnedPhrasal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('phrasal', models.CharField(verbose_name='phrasal', max_length=255, unique=True)),
                ('user', models.ForeignKey(verbose_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LearnedPresent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('verb', models.CharField(verbose_name='Present', max_length=255, unique=True)),
                ('category', models.CharField(verbose_name='Type', max_length=255, default='Regular')),
                ('user', models.ForeignKey(verbose_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Past',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('verb', models.CharField(verbose_name='Past', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PastParticiple',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('verb', models.CharField(verbose_name='Past participle', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhrasalVerb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('phrasal_verb', models.CharField(verbose_name='Phrasal Verb', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('verb', models.CharField(verbose_name='Present', max_length=255, unique=True)),
                ('category', models.CharField(verbose_name='Type', max_length=255, default='Regular')),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nombre de la rutina', max_length=255, unique=True)),
                ('user', models.ForeignKey(verbose_name='Usuario', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SentencePhrasalVerb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sentence', models.TextField(verbose_name='Sentence', unique=True)),
                ('secondary_id', models.CharField(verbose_name='Secondary Id', max_length=50)),
                ('auxiliary', models.CharField(verbose_name='Auxiliary', max_length=50)),
                ('phrasal_verb', models.ForeignKey(verbose_name='Present', to='practise.PhrasalVerb')),
            ],
        ),
        migrations.CreateModel(
            name='SentencePresent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sentence', models.TextField(verbose_name='Sentence', unique=True)),
                ('secondary_id', models.CharField(verbose_name='Secondary Id', max_length=50)),
                ('auxiliary', models.CharField(verbose_name='Auxiliary', max_length=50)),
                ('verb', models.ForeignKey(verbose_name='Present', to='practise.Present')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Tema', max_length=512, unique=True, default='--------------------', choices=[('VERBS', 'VERBS'), ('--------------------', '--------------------'), ('LEARNED WORD', 'LEARNED WORD'), ('VOCABULARY', 'VOCABULARY'), ('LEARNED PRESENT', 'LEARNED PRESENT'), ('LEARNED PHRASAL', 'LEARNED PHRASAL')])),
                ('repetitions', models.IntegerField(verbose_name='Repeticiones', default=5)),
                ('routine', models.ForeignKey(verbose_name='Rutina', to='practise.Routine')),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('word', models.CharField(verbose_name='Palabra', max_length=255)),
                ('learned', models.BooleanField(verbose_name='¿Aprendido?', default=False)),
                ('routine', models.ForeignKey(verbose_name='Tema', to='practise.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='pastparticiple',
            name='present',
            field=models.ForeignKey(verbose_name='Present', to='practise.Present'),
        ),
        migrations.AddField(
            model_name='past',
            name='present',
            field=models.ForeignKey(verbose_name='Present', to='practise.Present'),
        ),
    ]
