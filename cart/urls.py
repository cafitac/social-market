from django.urls import path

from cart.views import get_carts

urlpatterns = [
    path('cart', get_carts, name='get-carts'),
]
