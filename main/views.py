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

def reports(request):   
    return render(request, "reports.html")

def create_report(request):   
    return render(request, "create_report.html")

def consult_report(request):   
    return render(request, "consult_report.html")
