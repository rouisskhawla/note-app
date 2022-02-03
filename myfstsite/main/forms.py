from django.forms import ModelForm
from django import forms
from main.models import Note

class AddNote(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']

