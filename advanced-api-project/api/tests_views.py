from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    """Test suite for Book API endpoints"""

    def setUp(self):
        """Set up test data before each test"""
        self.client = APIClient()

        # Create test users
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.admin = User.objects.create_superuser(username="admin", password="admin123")

        # Create some book entries
        self.book1 = Book.objects.create(title="Django for Beginners", author="William S.", publication_year=2021)
        self.book2 = Book.objects.create(title="Learning Django REST", author="Jane Doe", publication_year=2022)

        # API URLs
        self.book_list_url = "/api/books/"
        self.book_detail_url = f"/api/books/{self.book1.id}/"
        self.book_create_url = "/api/books/create/"
        self.book_update_url = f"/api/books/update/{self.book1.id}/"
        self.book_delete_url = f"/api/books/delete/{self.book1.id}/"

    ## ✅ TEST: LIST BOOKS (GET)
    def test_list_books(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return 2 books

    ## ✅ TEST: GET SINGLE BOOK (GET)
    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    ## ✅ TEST: CREATE BOOK (POST) (Only Authenticated Users)
    def test_create_book_authenticated(self):
        """Test that authenticated users can create a book"""
        self.client.force_authenticate(user=self.user)
        data = {"title": "New Django Book", "author": "John Smith", "publication_year": 2023}
        response = self.client.post(self.book_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book"""
        data = {"title": "Unauthorized Book", "author": "Unknown", "publication_year": 2024}
        response = self.client.post(self.book_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ## ✅ TEST: UPDATE BOOK (PUT)
    def test_update_book(self):
        """Test updating a book"""
        self.client.force_authenticate(user=self.user)
        updated_data = {"title": "Updated Django Book", "author": "Updated Author", "publication_year": 2025}
        response = self.client.put(self.book_update_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    ## ✅ TEST: DELETE BOOK (DELETE)
    def test_delete_book(self):
        """Test deleting a book"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    ## ✅ TEST: FILTERING BY AUTHOR (GET)
    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        response = self.client.get(f"{self.book_list_url}?author=William S.")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "William S.")

    ## ✅ TEST: SEARCH BOOKS (GET)
    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(f"{self.book_list_url}?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    ## ✅ TEST: ORDERING BOOKS (GET)
    def test_order_books_by_year(self):
        """Test ordering books by publication year"""
        response = self.client.get(f"{self.book_list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(response.data[0]["publication_year"], response.data[1]["publication_year"])

