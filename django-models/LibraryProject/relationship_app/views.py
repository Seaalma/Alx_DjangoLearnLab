# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# Login View
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Logout View
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"

# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the newly registered user
            return redirect("home")  # Redirect to a page after login
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})
