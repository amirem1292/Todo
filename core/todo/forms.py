from django import forms
from .models import *

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['is_done']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
