from django.urls import path
from .views import add_comment, CommentUpdateView, CommentDeleteView
from .views import search_posts, posts_by_tag

urlpatterns = [
    path("post/<int:post_id>/comment/", add_comment, name="add-comment"),
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="edit-comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"),
    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', posts_by_tag, name='posts_by_tag'),
]

