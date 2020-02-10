from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    decsription = models.TextField()
    status = models.CharField(max_length=50)
    price = models.FloatField()
    
    def __str__(self):
        return self.title

class OrderProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    projects = models.ManyToManyField(OrderProject)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username