# general imports
from django.urls import path
from harvests.views import people, vehicles, origin, harvests,bunchbatch,bunch,sensor,bunchcategory

# api imports

# api urls

# general urls
urlpatterns = [
    path('harvests', harvests, name="harvests"),
    path('people', people, name="people"),
    path('vehicles', vehicles, name="vehicles"),
    path('origin', origin, name="origin"),
    path('bunchbatch', bunchbatch, name="bunchbatch"),
    path('bunch', bunch, name="bunch"),
    path('sensor', sensor, name="sensor"),
    path('bunchcategory', bunchcategory, name="bunchcategory"),
    
]
