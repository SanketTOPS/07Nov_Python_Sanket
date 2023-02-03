from django import forms
from .models import userSignup


class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'