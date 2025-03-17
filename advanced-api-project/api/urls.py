from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import views
urlpatterns = [
    path("books/", ListView.as_view(), name="book-list"),
    path("books/create/", CreateView.as_view(), name="book-create"),
    path("books/update/<int:pk>/", UpdateView.as_view(), name="book-update"),  # Ajustement ici
    path("books/delete/<int:pk>/", DeleteView.as_view(), name="book-delete"),  # Ajustement ici
    path("books/<int:pk>/", DetailView.as_view(), name="book-detail"),
    path('some_endpoint/', views.some_view, name='some_view'),
]



