from django import forms
from common.models import Invitation, Paper, Project, FinanceRound

class FinanceRoundForm(forms.ModelForm):
    class Meta:
        model = FinanceRound
        fields = ['title', 'brief', 'fundings_gathered', 'end_date']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

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

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'brief','is_public','content','required_money','type','project_scope']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tytuł'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Szczegółowy opis'}),
            'brief': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Krótki opis'}),
            'project_scope': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Zakres projektu'}), 
            'is_public': forms.CheckboxInput(),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Type'}),
            # 'profiles': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the view
        super().__init__(*args, **kwargs)

        if user:
            # Set the initial value for the author field to the logged-in user
            self.fields['author'] = forms.CharField(initial=user.profile_set,
                                                    widget=forms.HiddenInput())  # You can make it hidden or display it
            self.instance.author = user  # Set the author when saving the instance
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:  # Assign the user to the instance
            instance.user = self.user
        if commit:
            instance.save()
        return instance