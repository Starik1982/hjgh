# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-11 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0019_auto_20180509_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiro',
            name='image_skill',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='hiro',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
