# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guild_members', '0002_auto_20171221_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='BgResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField(default=1)),
                ('bg_date', models.DateTimeField(auto_now_add=True)),
                ('nickname', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='guild_members.GuildMembers')),
            ],
        ),
    ]
