# general imports
from django.urls import path
from reports.views import reports, create_report, query_report

# api imports

# api urls

# general urls
urlpatterns = [
    path('reports', reports, name="reports"),
    path('create_report', create_report, name="create_report"),
    path('query_report', query_report, name="query_report"),
]
