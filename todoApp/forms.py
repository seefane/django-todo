from django import forms
from django.forms import ModelForm, widgets
from .models import Task

#CreatePostForm
class CreateTaskForm(ModelForm):

    class Meta:
        model=Task
        fields = ['title','description','due_date']
        widgets = {
            'due_date': widgets.DateTimeInput(attrs={'type': 'datetime'})
        }
