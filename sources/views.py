from django.shortcuts import render
from .models import Vehicle
from .forms import VehicleForm

#Create your views here.
def vehicles(request): 
   vehicles = Vehicle.objects.all()
   context = {'vehicles':vehicles}  
   return render(request, "vehicles.html", context)

def crud_vehicle(request):

   form = VehicleForm()
   
   if request.method == 'POST':
      form = VehicleForm(request.POST)
      if form.is_valid():
         form.save()

   context = {'form':form}  
   return render(request, "crud_vehicle.html", context)

def parcel(request):   
   return render(request, "parcel.html")