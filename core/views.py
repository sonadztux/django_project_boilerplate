from django.shortcuts import render

from .models import Project

def index(request):
    return render(request, 'index.html')

def project_all(request):
    return render(request, "project-list.html")

def project_detail(request):
    return render(request, "product-page.html")