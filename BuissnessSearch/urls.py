from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.simple_view, name='simple_view'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('project/<int:id>/edit/', views.edit_project, name='edit_project'),


]