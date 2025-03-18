from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment
from .forms import CommentForm

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign logged-in user as author
        form.instance.post_id = self.kwargs["post_id"]  # Assign post ID from URL
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()
