from django.shortcuts import render
from common.models import Profile

def home(request):
    logged_user = request.user
    is_scientist = logged_user.profile_set.filter(type='scientist').exists()
    is_businessman = logged_user.profile_set.filter(type='businessman').exists()
    return render(request, 'start_page/home.html', context={'is_scientist': is_scientist, 'is_businessman': is_businessman})