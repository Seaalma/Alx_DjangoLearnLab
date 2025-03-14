# bookshelf/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# Example: A view to edit a book that requires the 'can_edit' permission
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        # Handle editing logic here
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('book_detail', book_id=book.id)
    
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# Example: A view to create a book that requires the 'can_create' permission
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    
    return render(request, 'bookshelf/create_book.html')
