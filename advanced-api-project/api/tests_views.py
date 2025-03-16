from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book
from rest_framework.test import APIClient
class BookAPITestCase(APITestCase):

    def setUp(self):
        """Setup test data and client"""
        self.client = APIClient()
        
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)  # Authenticate the client
        
        # Create test book instance
        self.book = Book.objects.create(title="Test Book", author="John Doe", publication_year=2024)

        # API Endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

    def test_list_books(self):
        """Test retrieving all books (GET /api/books/)"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Expected status: 200

    def test_create_book(self):
        """Test creating a book (POST /api/books/)"""
        data = {"title": "New Book", "author": "Jane Doe", "publication_year": 2025}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Expected status: 201

    def test_get_book_detail(self):
        """Test retrieving a single book by ID (GET /api/books/<id>/)"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        """Test updating a book (PUT /api/books/<id>/)"""
        data = {"title": "Updated Book", "author": "John Doe", "publication_year": 2024}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        """Test deleting a book (DELETE /api/books/<id>/)"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books(self):
        """Test filtering books by author (GET /api/books/?author=John Doe)"""
        response = self.client.get(f"{self.list_url}?author=John Doe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_books(self):
        """Test searching books by title (GET /api/books/?search=Test)"""
        response = self.client.get(f"{self.list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books(self):
        """Test ordering books by title (GET /api/books/?ordering=title)"""
        response = self.client.get(f"{self.list_url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permissions(self):
        """Test that unauthenticated users cannot create, update, or delete books"""
        self.client.logout()
        response = self.client.post(self.list_url, {"title": "Unauthorized Book", "author": "Jane", "publication_year": 2025})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


