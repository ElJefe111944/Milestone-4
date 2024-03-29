from django.urls import path
from . import views
from .views import ReviewCreateView

urlpatterns = [
    path(
        'all_watches/<int:pk>/add_review/',
        ReviewCreateView.as_view(), name='add_review'
    ),
    path('', views.all_watches, name='watches'),
    path('<int:watch_id>/', views.watch_detail, name='watch_detail'),
    path('add/', views.add_watch, name='add_watch'),
    path('edit/<int:watch_id>/', views.edit_watch, name='edit_watch'),
    path('delete/<int:watch_id>/', views.delete_watch, name='delete_watch'),
]
