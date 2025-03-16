from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book  # Ensure this is the correct import path

class BookAPITestCase(TestCase):
    """Test case for Book model API endpoints"""

    def setUp(self):
        """Set up test data and client"""
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Authenticate user
        self.client.force_authenticate(user=self.user)

        # Create test books
        self.book1 = Book.objects.create(title="Book One", author="Author One", price=10.99)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", price=15.50)

        # Define API endpoint
        self.book_list_url = "/api/books/"  # Adjust if necessary
        self.book_detail_url = f"/api/books/{self.book1.id}/"

    def test_create_book(self):
        """Test creating a book"""
        data = {"title": "New Book", "author": "New Author", "price": 20.00}
        response = self.client.post(self.book_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])

    def test_get_book_list(self):
        """Test retrieving book list"""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        """Test retrieving a single book"""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_update_book(self):
        """Test updating a book"""
        updated_data = {"title": "Updated Book", "author": "Updated Author", "price": 25.99}
        response = self.client.put(self.book_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], updated_data["title"])

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books(self):
        """Test filtering books by title"""
        response = self.client.get(self.book_list_url, {"title": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books(self):
        """Test searching books by author"""
        response = self.client.get(self.book_list_url, {"search": "Author Two"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author Two")

    def test_order_books(self):
        """Test ordering books by price"""
        response = self.client.get(self.book_list_url, {"ordering": "price"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(response.data[0]["price"], response.data[1]["price"])

    def test_authentication_required(self):
        """Test that authentication is required for protected endpoints"""
        self.client.logout()
        response = self.client.post(self.book_list_url, {"title": "Unauthorized Book", "author": "X", "price": 5})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
