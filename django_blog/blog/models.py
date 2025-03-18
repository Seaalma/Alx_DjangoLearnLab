from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = TaggableManager()  # Ajout de la gestion des tags

    def __str__(self):
        return self.title
