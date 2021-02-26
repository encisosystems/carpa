# general imports
from django.urls import path
from sources.views import vehicles, origin

# api imports

# api urls

# general urls
urlpatterns = [
    path('vehicles', vehicles, name="vehicles"),
    path('origin', origin, name="origin"),
]
