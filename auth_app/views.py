from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('secured')  # Redirect to a secured page
        else:
            return render(request, 'auth_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'auth_app/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Secured view
@login_required
def secured_view(request):
    return render(request, 'auth_app/secured_example.html')
