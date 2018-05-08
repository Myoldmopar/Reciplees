# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0003_auto_20180507_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.CharField(
                choices=[('0', ''), ('10', '\u215b'), ('30', '\t\xbc'), ('40', '\u2153'), ('50', '\xbd'),
                         ('55', '\u2154'), ('57', '\xbe'), ('60', '1'), ('65', '1 \xbd'), ('70', '2'), ('80', '3'),
                         ('90', '4'), ('100', '5'), ('110', '6'), ('120', '7'), ('130', '8'), ('140', '9'),
                         ('150', '10'), ('160', '15'), ('170', '20')], default='',
                help_text='The numeric part of the amount of this ingredient', max_length=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(
                choices=[('0', ''), ('5', 'Pinch'), ('10', 'tsp'), ('20', 'Tbsp'), ('30', 'c'), ('40', 'pint'),
                         ('50', 'qt'), ('60', 'liter'), ('70', 'gallon'), ('100', 'oz'), ('110', 'lb')], default='',
                help_text='The measurement portion of this ingredient', max_length=25),
        ),
    ]