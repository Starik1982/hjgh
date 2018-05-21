# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0014_remove_faq_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
