Vfrom rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookTests(APITestCase):

    def test_create_book(self):
        url = '/api/books/'
        data = {'title': 'Test Book', 'author': 'Test Author', 'isbn': '123456789'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')
