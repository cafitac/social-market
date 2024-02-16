from django.urls import include, path
from rest_framework import routers

from order.viewsets.order_viewset import OrderViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
]
