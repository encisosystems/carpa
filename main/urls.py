# general imports
from django.urls import path
from main.views import home, login, people, vehicles, origin, reports, create_report, consult_report

# api imports

# api urls

# general urls
urlpatterns = [
    path('', login, name="login"),
    path('home', home, name="home"),
    path('people', people, name="people"),
    path('vehicles', vehicles, name="vehicles"),
    path('origin', origin, name="origin"),
    path('reports', reports, name="reports"),
    path('create_report', create_report, name="create_report"),
    path('consult_report', consult_report, name="consult_report"),
]
