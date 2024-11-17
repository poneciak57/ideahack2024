from django.urls import path
from . import views

urlpatterns = [
    path('', views.publication_list, name='publication_list'),
    path('projects/',views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),
    path('add/', views.add_publication, name='add_publication'),
    path('projects/<int:project_id>/rounds', views.rounds, name='founding_rounds'),
    path('projects/<int:project_id>', views.project_details, name='project_details'), 
]