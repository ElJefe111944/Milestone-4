from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post

# Create your views here.


# def blog(request):
#     return render(request, 'blog/blog.html', {})


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/add_blog.html'
    fields = [
            'title', 'author', 'blog_image', 'subheading1',
            'main_content1', 'subheading2', 'main_content2'
            ]  