from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from common.models import CustomUser, Invitation, Paper, Profile, Project
from .forms import FinanceRoundForm, PublicationForm, ProjectForm
from django.contrib.auth.decorators import login_required

@login_required
def publication_list(request):
    logged_user = request.user
    # publications = Paper.objects.all()
    publications_of_logged_user = Paper.objects.filter(author__user=logged_user)
    publications_of_other_users = Paper.objects.exclude(author__user=logged_user)
    users = CustomUser.objects.all()
    return render(request, 'FbNaukowcy/publication_list.html',
                  {'publications_of_logged_user': publications_of_logged_user, 'publications_of_other_users': publications_of_other_users, 'users': users, 'logged_user': logged_user})

@login_required
def project_list(request):
    logged_user = request.user
    invitations = Invitation.objects.filter(receiver__user=logged_user)
    projects = Project.objects.all()
    users = Profile.objects.all()
    return render(request, 'FbNaukowcy/projects_list.html',
                  {'publications': projects, 'users': users, 'invitations': invitations, 'logged_user': logged_user})

@login_required
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
        form = ProjectForm(request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('publication_list')  # Przekierowanie na listę postów
    else:
        form = PublicationForm()
    return render(request, 'FbNaukowcy/add_project.html', {'form': form})

@login_required
def rounds(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = FinanceRoundForm(request.POST)
        if form.is_valid():
            finance_round = form.save(commit=False)
            finance_round.project = project
            finance_round.save()
            # TODO change to project details with project id in redirect
            # TODO also add funding rounds to project details view
            return redirect('project_list')
    else:
        form = FinanceRoundForm()
    return render(request, 'FbNaukowcy/add_round.html', {'form': form, 'project': project})

@login_required
def create_invitation(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    username = request.user
    user = get_object_or_404(CustomUser, username=username)
    profile = user.profile_set.first()
    if request.method == 'POST':
        invitation = Invitation.objects.create(
            project=project,
            sender = profile,
            receiver = CustomUser.objects.get(username=request.POST['receiver']).profile_set.first(),
            status = 'pending',
            message=request.POST['message'])
        invitation.save()
    return render(request, 'FbNaukowcy/create_invitation.html', {})