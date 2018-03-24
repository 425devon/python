# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..loginReg.models import User

# Create your models here.
class NoteManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["title"] = "Please add a title"
        if len(postData['desc']) < 1:
            errors["desc"] = "Please add a description"
        return errors

class Note(models.Model):
    topic = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    left = models.IntegerField(default=700)
    top = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(User, related_name="created_notes")
    objects = NoteManager()

