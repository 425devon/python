# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime 

# Create your views here.

def index(request):
    return render(request,'amadon/home.html')

def checkout(request):

    return render(request,'amadon/checkout.html')

def shirt(request):
    request.session['current'] = 19.99 * int(request.POST['quantity'])
    request.session['total'] += (19.99 * int(request.POST['quantity']))
    request.session['shirt'] = request.POST['quantity']
    request.session['items'] += int(request.POST['quantity'])
    return redirect('/amadon/checkout')

def sweater(request):
    request.session['current'] = 29.99 * int(request.POST['quantity'])
    request.session['total'] += (29.99 * int(request.POST['quantity']))
    request.session['sweater'] = request.POST['quantity']
    request.session['items'] += int(request.POST['quantity'])
    return redirect('/amadon/checkout')

def cup(request):
    request.session['current'] = 4.99 * int(request.POST['quantity'])
    request.session['total'] += (4.99 * int(request.POST['quantity']))
    request.session['cup'] = request.POST['quantity']
    request.session['items'] += int(request.POST['quantity'])
    return redirect('/amadon/checkout')

def book(request):
    request.session['current'] = 49.99 * int(request.POST['quantity'])
    request.session['total'] += (49.99 * int(request.POST['quantity']))
    request.session['book'] = request.POST['quantity']
    request.session['items'] += int(request.POST['quantity'])
    return redirect('/amadon/checkout')