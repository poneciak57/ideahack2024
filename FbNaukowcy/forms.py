from django import forms
from common.models import Paper

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'brief','link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'brief': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),
        }

    def __init__(self, *args, **kwargs):
        # Extract the 'user' parameter from the keyword arguments
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:  # Assign the user to the instance
            instance.user = self.user
        if commit:
            instance.save()
        return instance