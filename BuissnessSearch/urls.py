from django.urls import path
from . import views

app_name = 'BuissnessSearch'
urlpatterns = [
    path('add/', views.add_project, name='add_project'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('project/<int:id>/edit/', views.edit_project, name='edit_project'),
    path('project/<int:id>/addround/', views.rounds, name='rounds'),
    path('',views.project_list, name='project_list'),

]