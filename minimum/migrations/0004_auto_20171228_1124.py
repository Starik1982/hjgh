# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0003_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.ImageField(default=None, upload_to='news_picture/'),
        ),
    ]
