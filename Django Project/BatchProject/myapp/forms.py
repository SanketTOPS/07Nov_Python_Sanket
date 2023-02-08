from django import forms
from .models import userSignup,mynotes,feedback

class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','username','password','city','state','mobile']


class notesform(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'
    
class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'