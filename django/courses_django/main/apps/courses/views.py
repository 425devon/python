from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

from models import *

def index(request):
  
  return render(request, 'courses/courses.html', {"newCourse": Course.objects.all() })

def create(request):
  if len(request.POST['name']) > 5 and len(request.POST['desc']) > 15:
    newCourse = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])

  return redirect('/courses')

def remove(request, id):
  {"rm": Course.objects.get(id = id)}

  return render(request, 'courses/verify.html', {"rm": Course.objects.get(id = id)})

def destroy(request, id):
  dcourse = Course.objects.get(id = id)
  dcourse.delete()
  return redirect('/courses')

