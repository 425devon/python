# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.core import serializers
from models import *
import random

# Create your views here.
def index(request):
    return render(request, 'djax/index.html')

def all_json(request):
    users = User.objects.all()
    users_json = serializers.serialize("json", users)
    return HttpResponse(users_json, content_type='application/json')

def all_html(request):
    users = User.objects.all()
    return render(request, "djax/all.html", {"users": users})

def findName(request):
    users =  User.objects.filter(first_name__startswith=request.POST['startsWith'])
    return render(request, "djax/all.html", {"users": users})

def create(request):
    users = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        age = random.randint(1, 101),
        email_address = request.POST['email'])
    return render(request, 'djax/all.html',{"users": User.objects.order_by("-id")})

