# general imports
from django.urls import path
from harvests.views import people, harvests,bunchbatch,bunch,bunchcategory

# api imports

# api urls

# general urls
urlpatterns = [
    path('harvests', harvests, name="harvests"),
    path('people', people, name="people"),
    path('bunchbatch', bunchbatch, name="bunchbatch"),
    path('bunch', bunch, name="bunch"),
    path('bunchcategory', bunchcategory, name="bunchcategory"),
]
