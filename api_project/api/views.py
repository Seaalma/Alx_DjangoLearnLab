from rest_framework.generics import ListAPIView  # Ensure this is imported
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):  # Ensure it extends ListAPIView
    queryset = Book.objects.all()  # Retrieves all books
    serializer_class = BookSerializer  # Uses the BookSerializer
