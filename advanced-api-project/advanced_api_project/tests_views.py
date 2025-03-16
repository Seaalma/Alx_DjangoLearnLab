from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test client and test data"""
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2001)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2005)

    def test_list_books(self):
        """Test retrieving book list"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """Test creating a new book"""
        self.client.force_authenticate(user=self.user)
        data = {"title": "New Book", "author": "Author C", "publication_year": 2010}
        response = self.client.post("/api/books/create/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        """Test updating a book"""
        self.client.force_authenticate(user=self.user)
        data = {"title": "Updated Book", "author": "Author A", "publication_year": 2020}
        response = self.client.put(f"/api/books/update/{self.book1.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/books/delete/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
