from django.shortcuts import render
from django.http import HttpResponse

def myfunction(request):
    return HttpResponse("Introduction to Django!")

def demofunction(request):
    return HttpResponse("WELCOME!")