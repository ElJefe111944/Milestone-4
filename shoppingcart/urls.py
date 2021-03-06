from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_shoppingcart, name='shoppingcart'),
    path('add/<item_id>/', views.add_to_shoppingcart,
         name='add_to_shoppingcart'),
    path('update/<item_id>/', views.update_shoppingcart,
         name='update_shoppingcart'),
    path('remove/<item_id>/', views.remove_from_shoppingcart,
         name='remove_from_shoppingcart'),
]
