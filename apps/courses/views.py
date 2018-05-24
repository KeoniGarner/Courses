from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages

# Create your views here.
def courses(request):
    return redirect(reverse("home"))

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "courses/index.html", context)

def create(request):
    errors = Course.objects.validations(request.POST)
    if (len(errors)):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse("home"))
    
    course = Course.objects.create(name=request.POST.get("name", False), desc=request.POST.get("desc", False))
    course.save()

    return redirect(reverse("home"))

def confirm(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, "courses/delete.html", context)

def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect(reverse("home"))