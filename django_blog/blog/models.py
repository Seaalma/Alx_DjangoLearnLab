from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")  # Links to Post model
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to User model
    content = models.TextField()  # Stores comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-filled when created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-updated when edited

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
