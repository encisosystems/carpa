# general imports
from django.urls import path
from sources.views import vehicles, parcel, crud_vehicle


# api imports

# api urls

# general urls
urlpatterns = [
    path('vehicles', vehicles, name="vehicles"),
    path('parcel', origin, name="parcel"),
    path('crud_vehicle', crud_vehicle, name="crud_vehicle"),
]
