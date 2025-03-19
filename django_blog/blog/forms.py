from django import forms
from .models import Post
from taggit.forms import TagWidget  # Ajoutez cette ligne

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget())  # Utilisation du widget correct

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
