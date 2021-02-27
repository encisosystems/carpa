# general imports
from django.urls import path
from sources.views import vehicles, parcel,bunchbatch, bunch,sensor,bunchcategory

# api imports

# api urls

# general urls
urlpatterns = [
    path('vehicles', vehicles, name="vehicles"),
    path('parcel', origin, name="parcel"),
    path('bunchbatch', bunchbatch, name="bunchbatch"),
    path('bunch', bunch, name="bunch"),
    path('sensor', sensor, name="sensor"),
    path('bunchcategory', bunchcategory, name="bunchcategory"),
]
