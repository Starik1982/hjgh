# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guild_members', '0004_guildmembers_force'),
        ('bg_result', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_result', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bg_result.BgResult')),
                ('nickname', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='guild_members.GuildMembers')),
            ],
        ),
    ]
