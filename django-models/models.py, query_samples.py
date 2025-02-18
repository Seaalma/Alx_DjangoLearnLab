import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        return Book.objects.filter(author=author)
    return None

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.books.all()
    return None

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return Librarian.objects.filter(library=library).first()
    return None

# Example usage
if __name__ == "__main__":
    print("Books by George Orwell:", list(get_books_by_author("George Orwell")))
    print("Books in City Library:", list(get_books_in_library("City Library")))
    print("Librarian for City Library:", get_librarian_for_library("City Library"))

