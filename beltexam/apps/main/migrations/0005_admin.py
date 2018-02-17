# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180208_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admins_blogs', to='main.Friend')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='main.User')),
            ],
        ),
    ]