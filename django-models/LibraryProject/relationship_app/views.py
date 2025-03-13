from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Function to check if user is an Admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# View restricted to Admins
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")
    def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Function to check if a user is an Admin
def is_admin(user):
    return user.userprofile.role == "Admin"

# Function to check if a user is a Librarian
def is_librarian(user):
    return user.userprofile.role == "Librarian"

# Function to check if a user is a Member
def is_member(user):
    return user.userprofile.role == "Member"

# Admin view (restricted to Admin users)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# Librarian view (restricted to Librarian users)
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

# Member view (restricted to Member users)
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

