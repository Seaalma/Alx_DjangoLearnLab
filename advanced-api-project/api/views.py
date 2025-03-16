from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filter, search, and ordering functionality
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering by specific fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching (text-based) in these fields
    search_fields = ['title', 'author']

    # Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering (optional)
    ordering = ['title']  
