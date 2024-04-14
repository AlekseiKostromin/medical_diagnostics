from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:labtest_id>/', views.cart_add, name='cart_add'),

    path('increase-cart-item/<int:labtest_id>/', views.increase_cart_item, name='increase_cart_item'),
    path('decrease-cart-item/<int:labtest_id>/', views.decrease_cart_item, name='decrease_cart_item'),
    path('fetch-cart-count/', views.fetch_cart_count, name='fetch_cart_count'),
]
