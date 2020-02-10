from django.shortcuts import render

from .models import Project

def index(request):
    return render(request, 'eshopper/index.html')

def project_list(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, "home.html", context)

def project_detail(request):
    return render(request, "product-page.html")