from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # URL for listing all posts
    path('post/', PostListView.as_view(), name='post-list'),
    
    # URL for viewing a single post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # URL for creating a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    # URL for editing a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    
    # URL for deleting a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
