from django import forms
from .models import Activity, Project


class ActivityForm(forms.Form):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'title',
                                    'placeholder': 'Enter activity name'
                                }))

    project = forms.ModelChoiceField(queryset=Project.objects.all(
    ), widget=forms.Select(attrs={'class': 'project'}))


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'title-project',
                                    'placeholder': 'Enter Project name'
                                }))
