from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookTests(APITestCase):

    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_create_book(self):
        url = '/api/books/'
        data = {'title': 'Test Book', 'author': 'Test Author', 'isbn': '123456789'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(response.data['title'], 'Test Book')
        self.assertEqual(response.data['author'], 'Test Author')
        self.assertEqual(response.data['isbn'], '123456789')

    def test_get_book(self):
        book = Book.objects.create(title="Test Book", author="Test Author", isbn="123456789")
        url = f'/api/books/{book.id}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')
        self.assertEqual(response.data['author'], 'Test Author')
        self.assertEqual(response.data['isbn'], '123456789')

    def test_update_book(self):
        book = Book.objects.create(title="Old Title", author="Old Author", isbn="123456789")
        url = f'/api/books/{book.id}/'
        data = {'title': 'Updated Title', 'author': 'Updated Author', 'isbn': '987654321'}
        
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')
        self.assertEqual(response.data['author'], 'Updated Author')
        self.assertEqual(response.data['isbn'], '987654321')

    def test_delete_book(self):
        book = Book.objects.create(title="Test Book", author="Test Author", isbn="123456789")
        url = f'/api/books/{book.id}/'
        
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
