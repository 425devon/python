# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime 
import random 

casinoNum = random.randrange(-51,51)
farmNum = random.randrange(9,21)
cavNum = random.randrange(4,11)
houseNum = random.randrange(1,6)

# Create your views here.

def index(request):
    if 'alog' not in request.session:
        request.session['alog'] = "Welcome to ninja gold!"

    request.session['gold'] = 0

    return redirect('/gold/home')

def home(request):

    return render(request,'django_gold/index.html')


def farm(request):
    farmNum = random.randrange(9,21)
    request.session['gold'] += farmNum
    request.session['alog'] += ("\n earned {} gold from the farm!").format(farmNum)

    return redirect('/gold/home')

def cave(request):
    cavNum = random.randrange(4,11)
    request.session['gold'] += cavNum
    request.session['alog'] += ("\n You found {} gold in the cave!").format(cavNum)

    return redirect('/gold/home')

def house(request):
    houseNum = random.randrange(1,6)
    request.session['gold'] += houseNum
    request.session['alog'] += ("\n earned {} gold from the house!").format(houseNum)

    return redirect('/gold/home')

def casino(request):
    casinoNum = random.randrange(-51,51)
    request.session['alog'] += ("\n Tested your luck at the casino, {}").format(casinoNum)
    request.session['gold'] += casinoNum

    return redirect('/gold/home')