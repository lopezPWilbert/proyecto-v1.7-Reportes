# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20171120_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia_m',
            name='reportado',
            field=models.NullBooleanField(verbose_name='Reportado'),
        ),
    ]
