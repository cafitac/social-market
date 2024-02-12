from django.urls import include, path
from rest_framework import routers

from merchandise.viewsets.merchandise_viewset import MerchandiseViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('merchandises', MerchandiseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
