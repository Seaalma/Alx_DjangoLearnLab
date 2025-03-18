from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatiquement ajouté à la création
    updated_at = models.DateTimeField(auto_now=True)  # Automatiquement mis à jour

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
