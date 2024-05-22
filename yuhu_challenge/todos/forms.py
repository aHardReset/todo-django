from django import forms

from .models import ToDoItem


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = [
            "name",
            "description",
            "due_date",
        ]

        widgets = {
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class ToDoDelete(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ["id"]
