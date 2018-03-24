# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "helloooo i'm dojo_ninjas"
    return HttpResponse(response)
