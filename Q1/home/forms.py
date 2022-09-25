from dataclasses import fields
from django import forms
from .models import TaskManager

class ProjectForms(forms.ModelForm):
    class Meta:
        model = TaskManager
        fields = '__all__'