from django.shortcuts import render

# Create your views here.
def harvests(request):   
    return render(request, "harvests.html")

def people(request):   
    return render(request, "people.html")

def vehicles(request):   
    return render(request, "vehicles.html")

def origin(request):   
    return render(request, "origin.html")