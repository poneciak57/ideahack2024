from django.shortcuts import render, redirect
from .models import Publication
from .forms import PublicationForm
def publication_list(request):
    publications = Publication.objects.all().order_by('-created_at')
    return render(request, 'FbNaukowcy/publication_list.html', {'publications': publications})
def add_publication(request):
    if request.method == 'Publication':
        form = PublicationForm(request.Pub)
        if form.is_valid():
            form.save()
            return redirect('publication_list')  # Przekierowanie na listę postów
    else:
        form = PublicationForm()
    return render(request, 'FbNaukowcy/add_publication.html', {'form': form})