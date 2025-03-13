from relationship_app.models import Library, Book, Author, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Retrieve the author object
    return Book.objects.filter(author=author)  # Get books by this author

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # Get library
    return library.books.all()  # Return all books in this library

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Get library
    return library.librarian  # Return associated librarian


