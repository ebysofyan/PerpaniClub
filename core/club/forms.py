from django import forms
from core.orm.models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        exclude = ['']
