from django.contrib import admin
from .models import Category, ResFile, IsFavourite

# Register your models here.
admin.site.register(Category)
admin.site.register(ResFile)
admin.site.register(IsFavourite)