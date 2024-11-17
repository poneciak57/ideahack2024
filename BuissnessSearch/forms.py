# forms.py
from django import forms
from common.models import Project
class SimpleForm(forms.Form):
    text_input = forms.CharField(
        label='Enter Text',
        widget=forms.Textarea(attrs={'rows': 40, 'cols': 40})  # Adjust size as needed
    )
    file_input = forms.FileField(
        label='Upload File',
        required=False  # Make the file upload optional (can be set to True if required)
    )
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'required_money', 'brief']