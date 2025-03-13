# views.py
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Custom Logout View
class CustomLogoutView(LogoutView):
    next_page = 'login'

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('home')  # Redirect to a logged-in user's home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
