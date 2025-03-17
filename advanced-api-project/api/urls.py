from django.urls import path
from .views import ListView, DetailView, UpdateView, DeleteView
from django.urls import include, path

urlpatterns = [
    path("api/", include("api.urls")),  # Assure-toi que "api" est bien inclus]
    path("books/", ListView.as_view(), name="book-list"),
    path("books/<int:pk>/", DetailView.as_view(), name="book-detail"),
    path("books/<int:pk>/update/", UpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", DeleteView.as_view(), name="book-delete"),
]

