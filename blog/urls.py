from django.urls import path
# from . import views
from .views import BlogHomeView, BlogDetailView


urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('', BlogHomeView.as_view(), name='blog'),
]
