# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-10 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0010_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='preview_video',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
