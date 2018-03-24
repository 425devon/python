# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from random_words import RandomWords

rw = RandomWords()
word = rw.random_word()

# Create your views here.
def index(request):
    context ={
        "word": rw.random_words()[0]
    }
    
    return render(request,'random_words/word.html', context)

def create(request):
    request.session['count'] = request.session['count'] + 1
    return redirect('/')
