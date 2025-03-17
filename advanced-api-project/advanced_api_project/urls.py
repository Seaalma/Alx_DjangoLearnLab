from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path("books/", ListView.as_view(), name="book-list"),
    path("books/create/", CreateView.as_view(), name="book-create"),
    path("books/update/<int:pk>/", UpdateView.as_view(), name="book-update"),  # Ajustement ici
    path("books/delete/<int:pk>/", DeleteView.as_view(), name="book-delete"),  # Ajustement ici
    path("books/<int:pk>/", DetailView.as_view(), name="book-detail"),
]
from django.contrib import admin
from django.urls import path, include  # Make sure `include` is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Add this line to include your API URLs
]
