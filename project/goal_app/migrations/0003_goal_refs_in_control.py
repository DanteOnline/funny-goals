# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal_app', '0002_auto_20170424_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='refs_in_control',
            field=models.ManyToManyField(related_name='_goal_refs_in_control_+', to='goal_app.Goal'),
        ),
    ]
