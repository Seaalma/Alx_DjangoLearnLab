 from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
from django.views.generic import DetailView
from .models import Library

   context_object_name = "library"
template_name = "relationship_app/library_detail.html"

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
