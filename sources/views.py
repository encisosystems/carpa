from django.shortcuts import render
from .models import Vehicle

# Create your views here.
def vehicles(request): 
    vehicles = Vehicle.objects.all()
    context = {'vehicles':vehicles}  
    return render(request, "vehicles.html", context)

def parcel(request):   
    return render(request, "parcel.html")
