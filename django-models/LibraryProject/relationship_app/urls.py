from django.urls import path
from .views.librarian_view import librarian_view

urlpatterns = [
    path('librarian-view/', librarian_view, name='librarian_view'),
]
from django.urls import path
from .views.member_view import member_view

urlpatterns = [
    path('member-view/', member_view, name='member_view'),
]

