# general imports
from django.urls import path
from sources.views import vehicles, parcel

# api imports

# api urls

# general urls
urlpatterns = [
    path('vehicles', vehicles, name="vehicles"),
    path('parcel', origin, name="parcel"),
    
]
