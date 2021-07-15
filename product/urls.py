from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('products',views.product_page , name= 'all_products'),
    path('ordersPlaced',views.orders_placed_page , name = 'all_placed_orders'),
    

]
