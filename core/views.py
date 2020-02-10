from django.shortcuts import render

from .models import Project

def index(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'promotin/index.html', context)

def signup_umkm(request):
    return render(request, 'allauth/account/signup-umkm.html')

def signup_influencer(request):
    return render(request, 'allauth/account/signup-influencer.html')

def project_all(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'promotin/project-list.html', context)

def project_detail(request):
    return render(request, 'promotin/product-page.html')

def influencer_all(request):
    return render(request, 'promotin/influencer-list.html')