# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-18 15:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bg_result', '0011_delete_bgday'),
    ]

    operations = [
        migrations.CreateModel(
            name='BgDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_day', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
