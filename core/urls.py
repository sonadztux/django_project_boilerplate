from django.urls import path
from .views import project_list, project_detail, index

app_name = 'core'

urlpatterns = [
    # path('', project_list, name='project-list'),
    path('', index, name='index'),
    path('project/detail/', project_detail, name='project-detail')
]