# general imports
from django.urls import path
from main.views import home, login

# api imports

# api urls

# general urls
urlpatterns = [
    path('', login, name="login"),
    path('home', home, name="home"),
]
