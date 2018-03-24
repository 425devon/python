# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime 

def index(request):
    response = "i'm book authors app"
    return HttpResponse(response)
