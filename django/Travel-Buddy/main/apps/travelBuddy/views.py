from django.shortcuts import render, HttpResponse, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from ..loginReg.models import User
import bcrypt


def index(request):
    context={
    "myTrips": Trip.objects.all().filter(creator_id = request.session['user_id']),
    "joinedTrips": Schedule.objects.all(),
    "otherTrips": Trip.objects.all().exclude(creator_id = request.session['user_id']),
    }
    return render(request, 'travelBuddy/index.html', context)


def add(request):
    return render(request, 'travelBuddy/addPlan.html')

def newTrip(request):
    if len(request.POST['destination']) < 1:
        messages.add_message(request, messages.WARNING, 'Please Choose A Destination')
        return redirect('/travels/add')
    if len(request.POST['desc']) < 1:
        messages.add_message(request, messages.WARNING, 'Please enter A Description')
        return redirect('/travels/add')
    if len(request.POST['dateFrom']) < 1:
        messages.add_message(request, messages.WARNING, 'Please Choose A starting Date')
        return redirect('/travels/add')
    if len(request.POST['dateTo']) > 0 and len(request.POST['dateFrom']) < 1:
        messages.add_message(request, messages.WARNING, 'Please Choose A starting Date')
        return redirect('/travels/add')
    elif len(request.POST['dateTo']) < 1:
        messages.add_message(request, messages.WARNING, 'Please Choose An end Date')
        return redirect('/travels/add')
    
    Trip.objects.create(
        destination = request.POST['destination'],
        desc = request.POST['desc'],
        dateFrom = request.POST['dateFrom'],
        dateTo = request.POST['dateTo'],
        creator_id = request.session['user_id'])
    
    return redirect('/travels')

def destination(request, id):
    context={
        "dest": Trip.objects.get(id = id),
        "members": Schedule.objects.all().filter(trip_id = id)
    }

    return render(request, 'travelBuddy/destination.html', context)

def join(request, id):
    if len(Schedule.objects.filter(member_id = request.session['user_id']).filter(trip_id =id)) == 0:
        Schedule.objects.create(
            member_id = request.session['user_id'],
            trip_id = id)

        messages.add_message(request, messages.SUCCESS, 'Thanks for joining!')
    else:
        messages.add_message(request, messages.WARNING, "You've already joined!")
    return redirect('/travels')


def clear(request):
    request.session.flush()
    return redirect('/')

