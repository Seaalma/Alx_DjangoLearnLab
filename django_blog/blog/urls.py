from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    # ✅ Ensure correct and intuitive URL structure for comments
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="add-comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="edit-comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"),
]
