# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-09 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0066_setting_speaker_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertraining',
            name='agreement',
            field=models.BooleanField(default=False, verbose_name='Anlaşma kabul durumu'),
        ),
    ]
