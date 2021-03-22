from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .forms import PostForm, EditForm

from .models import Post

# Create your views here.


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-publish_date']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_blog.html'


class BlogUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/edit_blog.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog')
