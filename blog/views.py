from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .forms import PostForm, EditForm

from .models import Post, Category

# Create your views here.


# def blog(request):
#     return render(request, 'blog/blog.html', {})


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


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'


# def CategoryView(request, cats):
#     category_posts = Post.objects.filter(category=cats)
#     return render(request, 'blog/blog.html', {'cats': cats, 'category_posts': category_posts})
