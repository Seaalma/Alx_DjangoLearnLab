from django.urls import path
from .views import add_comment, edit_comment, delete_comment, post_detail

urlpatterns = [
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/<int:post_id>/comments/new/', add_comment, name='add_comment'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
