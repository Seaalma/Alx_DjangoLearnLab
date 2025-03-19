from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from django.urls import path
from .views import search_posts, posts_by_tag
from .views import PostByTagListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # ✅ Ensure correct and intuitive URL structure for comments
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="add-comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="edit-comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"),
    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', posts_by_tag, name='posts_by_tag'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
    
    # URL for viewing a single post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # URL for creating a new post
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    
    # URL for editing a post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    
    # URL for deleting a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


]

