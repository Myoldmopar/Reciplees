# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-27 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20180427_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.CharField(choices=[('0', ''), ('10', '\u215b'), ('30', '\t\xbc'), ('40', '\u2153'), ('50', '\xbd'), ('55', '\u2154'), ('57', '\xbe'), ('60', '1'), ('70', '2'), ('80', '3'), ('90', '4'), ('100', '5'), ('110', '6'), ('120', '7'), ('130', '8'), ('140', '9'), ('150', '10')], default='', max_length=5),
        ),
    ]
