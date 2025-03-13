book_to_delete = Book.objects.first()  # This grabs the first book
book_to_delete.delete()  # This deletes the book
Book.objects.all()
