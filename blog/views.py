from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect

from .models import Post

# Create your views here.


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))


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
