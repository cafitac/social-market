from django.urls import include, path
from rest_framework import routers

from cart.viewsets.cart_viewset import CartViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('carts', CartViewSet, basename='carts')


urlpatterns = [
    path('', include(router.urls)),
]
