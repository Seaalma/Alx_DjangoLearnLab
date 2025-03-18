from django.urls import path
from .views import add_comment, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path("post/<int:post_id>/comment/", add_comment, name="add-comment"),
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="edit-comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"),
]

