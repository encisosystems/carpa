from django.shortcuts import render
from .models import Vehicle

# Create your views here.
def vehicles(request): 
    vehicles = Vehicle.objects.all()
    context = {'vehicles':vehicles}  
    return render(request, "vehicles.html", context)

def origin(request):   
    return render(request, "origin.html")