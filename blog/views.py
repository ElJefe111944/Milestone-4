from django.views.generic import ListView, DetailView

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
