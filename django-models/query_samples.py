import os
import django

# Configurer Django pour exécuter des scripts indépendants
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Créer des exemples de données
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George Orwell")

book1 = Book.objects.create(title="Harry Potter", author=author1)
book2 = Book.objects.create(title="1984", author=author2)
book3 = Book.objects.create(title="Animal Farm", author=author2)

library1 = Library.objects.create(name="Central Library")
library1.books.add(book1, book2)

librarian1 = Librarian.objects.create(name="Alice", library=library1)

# 2. Requêtes demandées :

# a. Tous les livres d'un auteur spécifique
def books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return [book.title for book in books]

print("Books by George Orwell:", books_by_author("George Orwell"))

# b. Tous les livres d'une bibliothèque
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return [book.title for book in library.books.all()]

print("Books in Central Library:", books_in_library("Central Library"))

# c. Le bibliothécaire d'une bibliothèque
def librarian_of_library(library_name):
    librarian = Librarian.objects.get(library__name=library_name)
    return librarian.name

print("Librarian of Central Library:", librarian_of_library("Central Library"))

