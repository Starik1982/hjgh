# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-24 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0022_talent_talentupp'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='talentupp',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]