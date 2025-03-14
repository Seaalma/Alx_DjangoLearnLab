# bookshelf/views.py

from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()  # Save the form to the database
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})
