from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, "home.html")

def login(request):   
    return render(request, "login.html")

def people(request):   
    return render(request, "people.html")

def vehicles(request):   
    return render(request, "vehicles.html")

def origin(request):   
    return render(request, "origin.html")
