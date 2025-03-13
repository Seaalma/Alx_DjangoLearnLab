from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Function to check if the user is an Admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin-only view (inside views.py)
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")
