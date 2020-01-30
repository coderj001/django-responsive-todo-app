from django import forms
from .models import ToDoList

class FormToDoList(forms.ModelForm):
    class Meta:
        model=ToDoList
        fields=['item','status',]
