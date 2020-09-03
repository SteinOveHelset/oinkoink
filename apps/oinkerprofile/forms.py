from django import forms

from .models import OinkerProfile

class OinkerProfileForm(forms.ModelForm):
    class Meta:
        model = OinkerProfile
        fields = ('avatar',)