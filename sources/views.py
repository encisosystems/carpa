from django.shortcuts import render
from .models import Vehicle

# Create your views here.
def vehicles(request): 
    vehicles = Vehicle.objects.all()
    context = {'vehicles':vehicles}  
    return render(request, "vehicles.html", context)

def parcel(request):   
    return render(request, "parcel.html")

def bunchbatch(request):   
    return render(request, "bunchbatch.html")    

def bunch(request):   
    return render(request, "bunch.html")  

def sensor(request):   
    return render(request, "sensor.html")    

def bunchcategory(request):   
    return render(request, "bunchcategory.html")