# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_friend_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='users',
        ),
        migrations.AddField(
            model_name='friend',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='main.User'),
        ),
    ]
