from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like

class LikeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(user=self.user, content="Test Post")

    def test_like_post(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(f'/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.count(), 1)
