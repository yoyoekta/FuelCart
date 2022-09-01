import imp
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hi! This is a fuelcart web app.")
