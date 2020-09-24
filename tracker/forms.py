from django import forms
from .models import Tracker, Project


# class TrackForm(forms.ModelForm):

#     class Meta:
#         model = Tracker
#         fields = ['title', 'project']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['project'].queryset = Project.objects.all()

class TrackForm(forms.Form):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'xyz',
                                    'placeholder': 'Enter activity name'
                                }))

    project = forms.ModelChoiceField(queryset=Project.objects.all())
