from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = TaggableManager()  # Ajout de la gestion des tags

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.created_at}"

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()  # Update `updated_at` on save
        super().save(*args, **kwargs)

