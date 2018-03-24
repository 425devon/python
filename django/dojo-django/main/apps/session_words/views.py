# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime 

# Create your views here.
wordslist = []

def index(request):
    
    return render(request,'session_words/words.html')

def pickword(request):
        
    if len(request.POST['word']) > 0:
        wordObj = {
            "word": request.POST['word'],
            "color": request.POST['color'],
            "created_at": str(datetime.now()),
        }
    if 'big' in request.POST:
        wordObj['size'] = 40

    global wordslist
    wordslist.append(wordObj)
    request.session['allWords'] = wordslist

    print request.POST

    return redirect('/session_words')

def clear(request):
    request.session.clear()

    return redirect('/session_words')

