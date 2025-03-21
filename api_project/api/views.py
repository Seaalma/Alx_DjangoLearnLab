from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView): # Ensure it extends ListAPIView
    queryset = Book.objects.all()  # Retrieves all books
    serializer_class = BookSerializer  # Uses the BookSerializer
