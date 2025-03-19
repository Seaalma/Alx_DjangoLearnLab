from django import forms
from .models import Post
from taggit.forms import TagWidget  # Importer TagWidget
from django.forms import widgets  # ✅ Ajouter cette ligne
from .models import Comment
class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget())  # Utilisation correcte du widget pour les tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # You can add more fields if needed.

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content.strip():
            raise forms.ValidationError("Comment content cannot be empty.")
        return content

