# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-23 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0013_faq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='date',
        ),
    ]
