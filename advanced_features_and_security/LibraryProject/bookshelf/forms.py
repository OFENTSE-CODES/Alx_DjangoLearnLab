from django import forms
from .models import Book  # Or any model you are working with

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author'] 