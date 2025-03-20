from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from .views import search_posts, posts_by_tag
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
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/comments/new/', views.post_detail, name='add_comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
     path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    # Create a new comment
    path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),
    
    # Edit an existing comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='edit_comment'),
    
    # Delete an existing comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
    # Post detail and displaying comments
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # Create a new comment (fixing the expected pattern: "post/<int:pk>/comments/new/")
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),

    # Edit an existing comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='edit_comment'),

    # Delete an existing comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
 path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', posts_by_tag, name='posts_by_tag'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),

]

