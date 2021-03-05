from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_shoppingcart, name='shoppingcart'),
    path('add/<item_id>/', views.add_to_shoppingcart,
         name='add_to_shoppingcart'),
]
