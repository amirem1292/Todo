from django import forms
from .models import *

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['author', 'title']

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['is_done']