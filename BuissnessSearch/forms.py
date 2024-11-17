# forms.py
from django import forms
from common.models import Project, FinanceRound
class SimpleForm(forms.Form):
    text_input = forms.CharField(
        label='Enter Text',
        widget=forms.Textarea(attrs={'rows': 20, 'cols': 40})  # Adjust size as needed
    )
    file_input = forms.FileField(
        label='Upload File',
        required=False  # Make the file upload optional (can be set to True if required)
    )
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'required_money', 'brief']

class FinanceRoundForm(forms.ModelForm):
    class Meta:
        model = FinanceRound
        fields = ['title', 'brief', 'fundings_gathered', 'end_date']
        labels = {
            "brief": ""
        }
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
