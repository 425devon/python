# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context ={
    "date":strftime("%A-%B-%d"),
    "time":strftime('%I-%M-%p', gmtime()),
    }
    
    return render(request,'time_display/time.html', context)
