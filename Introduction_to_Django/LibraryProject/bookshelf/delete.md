# Deleting a Book and Confirming the Deletion

## Command:
The following commands were used to delete the book and confirm the deletion:

1. Delete the book:
```python
# Retrieve the first book and delete it
book_to_delete = Book.objects.first()
book_to_delete.delete()

# Verify that the book is deleted
all_books = Book.objects.all()
print(all_books)  # Expected Output: empty list or QuerySet
