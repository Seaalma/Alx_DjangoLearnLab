from django.contrib import admin
from .models import Book

# Define a custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields to be displayed in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Filters in the sidebar for easy categorization
    list_filter = ('author', 'publication_year')

    # Search bar functionality for title and author
    search_fields = ('title', 'author')

# Register the Book model with the customized admin options
admin.site.register(Book, BookAdmin)

