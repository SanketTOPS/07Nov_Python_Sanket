from django import forms
from .models import userInfo


class userinfoForm(forms.ModelForm):
    class Meta:
        model=userInfo
        fields='__all__'
