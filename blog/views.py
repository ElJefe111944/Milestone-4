from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect

from profiles.models import UserProfile
from .models import Post

# Create your views here.


def LikeView(request, pk):
    if request.user.is_authenticated:
        myPost = get_object_or_404(Post, pk=pk)
        session_user = request.user
        print("--------------session user:", session_user)
        user_like = get_object_or_404(User, pk=request.user.id)
        print("----------------user_like", user_like)
        like = myPost.likes.add(user_like)
        myPost.save()
        print("----------------Like:", like)
        return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))
 

class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-publish_date']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(BlogDetailView, self).get_context_data(**kwargs)

    #     stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    #     total_likes = stuff.total_likes()
    #     context["total_likes"] = total_likes
    #     return context


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
