from django.urls import path
from .views import login_view, logout_view, secured_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('secured_example/', secured_view, name='secured'),
]