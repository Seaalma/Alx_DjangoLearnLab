from django import forms
from .models import Post
from taggit.forms import TagWidget  # Importer TagWidget
from django.forms import widgets  # ✅ Ajouter cette ligne

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget())  # Utilisation correcte du widget pour les tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
