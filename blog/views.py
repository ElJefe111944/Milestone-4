from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .forms import PostForm, EditForm

from .models import Post

# Create your views here.


# def blog(request):
#     return render(request, 'blog/blog.html', {})


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-id']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_blog.html'
    # fields = [
    #         'title', 'author', 'blog_image', 'subheading1',
    #         'main_content1', 'subheading2', 'main_content2'
    #         ]  


class BlogUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/edit_blog.html'
    # fields = [
    #         'title', 'title_tag', 'blog_image', 'subheading1',
    #         'main_content1', 'subheading2', 'main_content2'
    #         ] 


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog')
