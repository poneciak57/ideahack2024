from django.shortcuts import render, redirect, HttpResponse
from common.models import Paper, Profile
from .forms import PublicationForm
def publication_list(request):
    publications = Paper.objects.all()

    users = Profile.objects.exclude().distinct()#chcemy dawać tylko podobnych użytkowników


    return render(request, 'FbNaukowcy/publication_list.html',
                  {'publications': publications, 'users': users})
def project_list(request):
    projects = Paper.objects.all()
    users = Profile.objects.exclude().distinct()
    return render(request, 'FbNaukowcy/projects_list.html',
                  {'publications': projects, 'users': users})

def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('publication_list')  # Przekierowanie na listę postów
    else:
        form = PublicationForm()
    return render(request, 'FbNaukowcy/add_publication.html', {'form': form})

def add_project(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('publication_list')  # Przekierowanie na listę postów
    else:
        form = PublicationForm()
    return render(request, 'FbNaukowcy/add_project.html', {'form': form})

def add_u(request):
    Profile.objects.create(type='sciencist',open_for_contact=True)
    return HttpResponse('ok')