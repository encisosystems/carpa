# general imports
from django.urls import path
from harvests.views import people, harvests

# api imports

# api urls

# general urls
urlpatterns = [
    path('harvests', harvests, name="harvests"),
    path('people', people, name="people"),
]
