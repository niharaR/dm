from  django import forms
from django.db import models
from .models import Task


class TodoForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date',]