from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, \
    DetailView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'description', 'image')
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'description', 'image')
    success_url = reverse_lazy('blog:list')


class BlogDelteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
