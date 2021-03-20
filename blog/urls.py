from django.urls import path
# from . import views
from .views import BlogHomeView, BlogDetailView, BlogCreateView


urlpatterns = [
    path('add_post', BlogCreateView.as_view(), name='add_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('', BlogHomeView.as_view(), name='blog'),
]
