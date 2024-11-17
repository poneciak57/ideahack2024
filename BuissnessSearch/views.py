# views.py
from django.shortcuts import render,get_object_or_404, redirect, reverse
import random
from .chat_utils import idea_to_vec, fill_gaps_from_info
from .forms import SimpleForm, ProjectForm
from common.models import Project, Profile
def add_project(request):
    print("XSDSD")
    if request.method == 'POST':
        form = SimpleForm(request.POST, request.FILES)  # Pass request.FILES to handle file data
        if form.is_valid():
            text = form.cleaned_data['text_input']
            file = form.cleaned_data['file_input']

            # Process the form data
            print(f"Received text: {text}")
            ans=text
            if file:
                # If a file was uploaded, handle it
                print(f"File uploaded: {file.name}")
                # You can save the file or perform other actions as needed
                # For example, saving to a model, or just storing it in the server
                ans=file.read()### przerabianie docsa na txt
            idea_type = idea_to_vec(ans)
            auto_fill = fill_gaps_from_info(ans)
            txt=""
            try:
                title,money,brief,type = auto_fill.split(';')
                if(type=="s"):
                    type="Startup"
                else:
                    type="Working Business"
            except Exception as e:
                txt=e
                title="tytuł"
                money='1000000'
                brief='super pomysł'
                type="Startup"
            user = request.user
            user = user.profile_set.first()
            new_project=Project(author = user, title=title,required_money=random.randint(5,100)*100000,brief=brief,type=type)
            new_project.save()
            id=new_project.pk
            return redirect('/buisness/project/'+str(id)+'/')
    else:
        form = SimpleForm()

    return render(request, 'BuissnessSearch/simple_view.html', {'form': form})

def edit_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', id=project.id)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'BuissnessSearch/edit_project.html', {'form': form, 'project': project})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'BuissnessSearch/project_detail.html', {'project': project})

def project_list(request):
    projects = Project.objects.all()
    users = Profile.objects.all()
    return render(request, 'BuissnessSearch/projects_list.html',
                  {'publications': projects, 'users': users})