# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelBuddy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='listed',
            field=models.ManyToManyField(related_name='ontrip', to='travelBuddy.Trip'),
        ),
    ]
