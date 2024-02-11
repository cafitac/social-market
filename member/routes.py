from django.urls import include, path
from rest_framework import routers

from member.viewsets import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
