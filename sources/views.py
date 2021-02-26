from django.shortcuts import render

# Create your views here.
def vehicles(request):   
    return render(request, "vehicles.html")

def origin(request):   
    return render(request, "origin.html")