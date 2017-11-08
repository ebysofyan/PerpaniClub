from django import forms
from core.orm.models import ClubFiles


class ClubFilesForm(forms.ModelForm):

    class Meta:
        model = ClubFiles
        fields = ['file']
