from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Function to check if user is a librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Librarian"

# Librarian view restricted to librarians only
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
