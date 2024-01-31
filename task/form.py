from django import forms
from .models import Task

class AddTask_Form(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','assigned_to','due_date','priority']
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter Task Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg','placeholder':'Enter Task Description'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control form-control-lg','type':'date'}),
            'priority': forms.Select(attrs={'class': 'form-control form-control-lg'}),
        }