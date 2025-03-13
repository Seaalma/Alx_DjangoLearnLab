from bookshelf.models import Book
Book.objects.all()
book_to_delete = Book.objects.first()  
book_to_delete.delete()  
Book.objects.all()
