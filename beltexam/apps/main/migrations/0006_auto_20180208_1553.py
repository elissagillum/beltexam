# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admins_friends', to='main.Friend'),
        ),
    ]