from django import forms
from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'brief','link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'brief': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),
        }