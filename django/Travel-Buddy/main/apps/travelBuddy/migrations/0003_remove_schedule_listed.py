# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 23:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelBuddy', '0002_schedule_listed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='listed',
        ),
    ]
