# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-13 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0020_auto_20180511_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiro',
            name='skill_title',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
