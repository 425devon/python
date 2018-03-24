# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    
    return render(request,'surveys/survey.html')

def process(request):
    request.session['count'] = request.session['count'] + 1
    print "recieved Post!!!"

    data = {
        "name": request.POST['name'],
        "location": request.POST['location'],
        "language": request.POST['language'],
        "comment": request.POST['comment']
    }

    return render(request,'surveys/result.html', data)

def back(request):
    return redirect('/surveys')
