from django.urls import path
from .views import librarian_view, member_view

urlpatterns = [
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
