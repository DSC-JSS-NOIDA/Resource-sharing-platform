from django.urls import path, include
from . import views

app_name = 'Resource'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.category_view, name="category_view"),
    path('all/', views.all_files_view, name="all_files_view"),
    path('filecreate/', views.FileCreate.as_view(), name="filecreate"),
    path('favourite/<int:file_id>/', views.is_favourite, name='is_favourite'),
    path('myfavourites/', views.favourite_view, name='favourite_view'),
    path('myuploads/', views.my_uploads, name='my_uploads'),
    path('download/<int:file_id>/', views.download, name='download'),
    path('search/', views.searchposts, name='searchposts'),
]


