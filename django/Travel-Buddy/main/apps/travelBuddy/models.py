# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..loginReg.models import User

# Create your models here.
class Trip(models.Model):
    creator = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    dateFrom = models.DateField()
    dateTo = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(User, related_name="created_trips")    

class Schedule(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    trip = models.ForeignKey(Trip, related_name="added_trip")
    member = models.ForeignKey(User, related_name="sc_user")

