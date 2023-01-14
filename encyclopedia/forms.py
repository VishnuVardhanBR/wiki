from django import forms
from django.forms import ModelForm, TextInput, EmailInput

class SearchForm(forms.Form):
    search = forms.CharField(label='Search Encyclopedia', required=False)

class CreateNewEntryForm(forms.Form):
    title = forms.CharField(label="Title", )
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type the content of the entry in markdown format.'}), label = "")
