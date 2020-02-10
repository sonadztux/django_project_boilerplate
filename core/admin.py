from django.contrib import admin

from .models import Project, OrderProject, Order

admin.site.register(Project)
admin.site.register(OrderProject)
admin.site.register(Order)