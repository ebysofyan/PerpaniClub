from django import forms
from core.orm.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['user', 'club']
