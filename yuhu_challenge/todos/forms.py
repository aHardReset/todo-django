from django import forms

from .models import ToDoItem


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ["name", "description"]


class ToDoDelete(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ["id"]
