from django.urls import path
from .views import index, project_all

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),

    path('project/all/', project_all, name='project-all'),
    # path('project/detail/', project_detail, name='project-detail')
]