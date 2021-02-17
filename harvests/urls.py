# general imports
from django.urls import path
from harvests.views import people, vehicles, origin

# api imports

# api urls

# general urls
urlpatterns = [
    path('people', people, name="people"),
    path('vehicles', vehicles, name="vehicles"),
    path('origin', origin, name="origin"),
]
