# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='in_future',
            new_name='in_control',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='in_future_reason',
        ),
        migrations.AddField(
            model_name='category',
            name='in_future',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='in_future_reason',
            field=models.TextField(blank=True),
        ),
    ]