from django import forms
from core.orm.models import SocialAccount

class SocialAccountForm(forms.ModelForm):
    class Meta:
        model = SocialAccount
        exclude = ['club']
