from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import BasePermission

# Custom permission to allow only the owner to update or delete a book
class IsBookOwner(BasePermission):
    """
    Custom permission to only allow the owner of a book to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  # Assuming the `Book` model has an `owner` field

# Create view (only accessible to authenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# Update view (only accessible to authenticated users and admins)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsBookOwner]  # Only authenticated users and the book owner can update

# Delete view (only accessible to admins)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]  # Only admins can delete books
