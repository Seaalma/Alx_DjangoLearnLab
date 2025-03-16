from rest_framework import generics, filters
from django_filters import rest_framework as django_filters  # ✅ Add this import
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # ✅ Add filter, search, and ordering
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # ✅ Enable filtering by these fields
    filterset_fields = ['title', 'author', 'publication_year']

    # ✅ Enable searching (text-based) in these fields
    search_fields = ['title', 'author']

    # ✅ Enable ordering by these fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
