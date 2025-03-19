from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm
from django.shortcuts import render
from django.db.models import Q
from .models import Post
from taggit.models import Tag
from django.views.generic import ListView
from django.shortcuts import get_object_or_404 

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'  # Assurez-vous d'avoir ce template
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
        return Post.objects.filter(tags=tag)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
        return context


def posts_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/posts_by_tag.html', {'tag': tag, 'posts': posts})

def search_posts(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()


    return render(request, 'blog/search_results.html', {'query': query, 'results': results})

# ✅ Already Added in Previous Step
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  
        form.instance.post_id = self.kwargs["post_id"]  
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

# ✅ Fixing the Missing `CommentUpdateView`
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/edit_comment.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # ✅ Only the author can edit

    def get_success_url(self):
        return self.object.post.get_absolute_url()

# ✅ Fixing the Missing `CommentDeleteView`
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/delete_comment.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # ✅ Only the author can delete
