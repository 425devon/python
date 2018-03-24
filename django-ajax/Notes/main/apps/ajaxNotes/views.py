# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core import serializers
from models import *
from ..loginReg.models import User
import bcrypt

def index(request):
    return render(request, 'ajaxNotes/index.html', {"notes": Note.objects.all().filter(creator_id = request.session['user_id'])})

def create(request):
    errors = Note.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/notes/note')
    else:
        Note.objects.create(
        topic=request.POST['topic'], 
        title=request.POST['title'], 
        desc=request.POST['desc'],
        creator_id = request.session['user_id'])
        return  render(request, 'ajaxNotes/note.html', {"notes": Note.objects.last()})

def location(request):
    print "still working"
    unote = Note.objects.get(id = request.POST['id'])
    unote.top = float(request.POST['top'])
    unote.left = float(request.POST['left'])
    unote.save()
    return redirect('/notes')

def delete(request, id):
    x = Note.objects.get(id = id)
    x.delete()
    return redirect('/notes')

def clear(request):
    request.session.flush()
    return redirect('/')