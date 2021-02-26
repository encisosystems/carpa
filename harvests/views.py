from django.shortcuts import render

# Create your views here.
def harvests(request):   
    return render(request, "harvests.html")

def people(request):   
    return render(request, "people.html")

    