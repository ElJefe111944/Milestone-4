from django.urls import path
# from . import views
from .views import (
    BlogHomeView, BlogDetailView, BlogCreateView,
    BlogUpdateView, BlogDeleteView, LikeView
  
    )


urlpatterns = [     
    path('add_post', BlogCreateView.as_view(), name='add_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('edit/post/<int:pk>/', BlogUpdateView.as_view(), name='edit_post'),
    path(
        'delete/post/<int:pk>/', BlogDeleteView.as_view(), name='delete_post'
        ),
    path('', BlogHomeView.as_view(), name='blog'),
    path('like/<int:pk>', LikeView, name='like-post'),
]
