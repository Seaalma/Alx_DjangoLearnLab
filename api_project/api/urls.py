from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView for books
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs (CRUD operations for books)
    path('', include(router.urls)),
]
