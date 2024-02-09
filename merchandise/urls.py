from django.urls import include, path
from rest_framework import routers

from merchandise.views import MerchandiseViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('merchandises', MerchandiseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
