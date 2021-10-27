from django.views.generic import DetailView, ListView
from .models import Post

# criando views com classes


class PostListView(ListView):
    models = Post

    def get_queryset(self):
        """Return Posts """
        return Post.objects.order_by('id')


class PostDetailView(DetailView):
    model = Post
