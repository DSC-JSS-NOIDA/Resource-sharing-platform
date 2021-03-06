from django.db import models
from django.urls import reverse, reverse_lazy
from .forms import User
from datetime import datetime


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=350, default= '' ,null = True)
    image = models.CharField(max_length=1000, default= '' ,null = True)
    def __str__(self):
        return self.category

class ResFile(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    category = models.ForeignKey(Category, null=True,  on_delete = models.SET_NULL)
    tags = models.CharField(max_length=500)
    file = models.FileField(upload_to='uploads/', null=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    downloads = models.IntegerField(default=0)
    def __str__(self):
        return self.title+' by '+self.uploader.username
    def get_absolute_url(self):
        return reverse('Resource:index')

class IsFavourite(models.Model):
    file = models.ForeignKey(ResFile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.file.title+' - '+self.user.username