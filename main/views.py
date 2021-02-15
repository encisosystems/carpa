from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return HttpResponse('<h1>It worked!</h1>'
                        '<div>Made by <a href="https://www.encisosystems.com" target="_blank">EncisoSystems</a></div>')

def login(request):   
    return render(request, "login.html")
