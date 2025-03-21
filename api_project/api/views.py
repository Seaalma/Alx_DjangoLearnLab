from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView): # Ensure it extends ListAPIView
    queryset = Book.objects.all()  # Retrieves all books
    serializer_class = BookSerializer  # Uses the BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.all()  # Retrieves all books
    serializer_class = BookSerializer  # Uses the BookSerializer
