from django.urls import path
from .views.librarian_view import librarian_view

urlpatterns = [
    path('librarian-view/', librarian_view, name='librarian_view'),
]
