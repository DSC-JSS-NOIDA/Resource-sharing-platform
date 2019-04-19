from django.urls import path, include
from . import views

app_name = 'Resource'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.category_view, name="category_view"),
    path('all/', views.all_files_view, name="all_files_view"),
    path('filecreate/', views.FileCreate.as_view(), name="filecreate"),
    
]