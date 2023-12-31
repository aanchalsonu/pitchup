# forms.py
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label='Search',
        widget=forms.TextInput(attrs={'class': 'form-control me-2', 'placeholder': 'Search'}),
    )
