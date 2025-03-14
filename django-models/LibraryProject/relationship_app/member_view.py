from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Function to check if user is a member
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Member"

# Member view restricted to members only
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
