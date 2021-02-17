from django.shortcuts import render

# Create your views here.
def reports(request):   
    return render(request, "reports.html")

def create_report(request):   
    return render(request, "create_report.html")

def query_report(request):   
    return render(request, "query_report.html")
