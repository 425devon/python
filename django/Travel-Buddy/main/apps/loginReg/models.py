# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First name should be more than 2 characters."
        if len(postData['last_name']) < 3:
            errors['last_name'] = "Last name should be more than 2 characters."
        if len(str(postData['password'])) < 8:
            errors['password'] = "Password must be atleast 8 charaters long."
        if str(postData['password']) != str(postData['cpassword']):
            errors['match'] = "Passwords do not match!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

