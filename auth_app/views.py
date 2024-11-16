from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegistrationForm
from common.models import Profile
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
            return render(request, 'auth_app/login.html', {'error': 'Nieprawidłowy login lub hasło'})
    return render(request, 'auth_app/login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()

            # Create the profile linked to the user
            profile_type = form.cleaned_data['profile_type']
            Profile.objects.create(
                user=user,
                type=profile_type,
                open_for_contact=True  # You can adjust this based on your form or set a default value
            )

            # Success message
            # messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to login or another page after registration
        # else:
            # messages.error(request, 'There was an error with your registration. Please check the form.')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'auth_app/register.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Secured view
@login_required
def secured_view(request):
    return render(request, 'auth_app/secured_example.html')
