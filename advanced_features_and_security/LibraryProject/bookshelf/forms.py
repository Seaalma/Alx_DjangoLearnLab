# bookshelf/forms.py

from django import forms
from .models import Book  # If you want to create a form for the Book model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # You can replace this with the model you are using
        fields = ['title', 'author']  # Include fields you want in the form
