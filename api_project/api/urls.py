from django.urls import path
from .views import BookList  # Ensure BookList is imported

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
