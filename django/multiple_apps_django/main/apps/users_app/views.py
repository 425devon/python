# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = "a placeholder to displat a list of all the users"
    return HttpResponse(response)

def login(request):
    response = "a placeholder for users to login"
    return HttpResponse(response)

def new(request):
    return redirect('/users')

def register(request):
    response = "placeholder for user to create a new user record"
    return HttpResponse(response)
