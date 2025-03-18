from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm

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
