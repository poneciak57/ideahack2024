# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from common.models import CustomUser
from common.models import Profile

class CustomUserRegistrationForm(UserCreationForm):
    # Extra fields
    links = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter URLs, one per line'}),
        required=False,
        label='Links (optional)',
    )
    
    # Add a field for selecting profile type
    profile_type = forms.ChoiceField(
        choices=Profile.PROFILE_TYPE_CHOICES,  # Use the same choices as the Profile model
        label='Profile Type',
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'links', 'profile_type']

    def clean_links(self):
        links = self.cleaned_data.get('links')
        if links:
            # Split by line and filter out empty strings if any
            return [link.strip() for link in links.splitlines() if link.strip()]
        return []