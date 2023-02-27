from django import forms
from django.forms import ModelForm
from .models import Task
from django.forms import widgets


class ReminderCreateForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ReminderAssignForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'owner']
        widgets = {
            'due_date': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ReminderUpdateForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description',
                  'due_date', 'is_finished', 'is_notified']
        widgets = {
            'due_date': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
