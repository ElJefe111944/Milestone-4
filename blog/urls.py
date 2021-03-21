from django.urls import path
# from . import views
from .views import BlogHomeView, BlogDetailView, BlogCreateView, BlogUpdateView


urlpatterns = [
    path('add_post', BlogCreateView.as_view(), name='add_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('edit/post/<int:pk>/', BlogUpdateView.as_view(), name='edit_post'),
    path('', BlogHomeView.as_view(), name='blog'),
]
