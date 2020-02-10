from django.shortcuts import render

from .models import Project

def index(request):
    return render(request, 'promotin/index.html')

def signup_umkm(request):
    return render(request, 'allauth/account/signup-umkm.html')

def signup_influencer(request):
    return render(request, 'allauth/account/signup-influencer.html')

def project_all(request):
    return render(request, 'promotin/project-list.html')

def project_detail(request):
    return render(request, 'promotin/product-page.html')

def influencer_all(request):
    return render(request, 'promotin/influencer-list.html')