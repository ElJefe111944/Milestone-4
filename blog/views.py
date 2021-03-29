from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from .forms import PostForm, EditForm, CommentForm
from django.http import HttpResponseRedirect

# from profiles.models import UserProfile
from .models import Post, Comment

# Create your views here.


def LikeView(request, pk):
    if request.user.is_authenticated:
        myPost = get_object_or_404(Post, pk=pk)       
        user_like = get_object_or_404(User, pk=request.user.id)
        if myPost.likes.filter(id=request.user.id).exists():
            myPost.likes.remove(request.user)
        else:     
            myPost.likes.add(request.user)
            myPost.save()
    
        return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))
 

class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-publish_date']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


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


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('blog')


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'
    success_url = reverse_lazy('blog')
