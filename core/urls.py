from django.urls import path
from .views import index, signup_umkm, signup_influencer, project_all, project_detail, influencer_all

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),

    path('accounts/signup/umkm/', signup_umkm, name='signup_umkm'),
    path('accounts/signup/influencer/', signup_influencer, name='signup_influencer'),

    path('project/all/', project_all, name='projects'),
    path('project/detail/', project_detail, name='project_detail'),

    path('influencer/all/', influencer_all, name='influencers')
]
