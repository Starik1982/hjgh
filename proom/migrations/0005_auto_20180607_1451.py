# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-07 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proom', '0004_auto_20180604_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalroom',
            name='fburls',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='personalroom',
            name='insturls',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='personalroom',
            name='vkurls',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
