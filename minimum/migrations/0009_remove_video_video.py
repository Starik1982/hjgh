# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-10 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0008_auto_20180307_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
    ]
