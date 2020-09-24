from django import forms


class TrackForm(forms.Form):
    title = forms.CharField(max_length=50,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'xyz',
                                   'placeholder': 'Enter activity name'
                               }))
