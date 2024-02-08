from django.urls import include, path
from rest_framework import routers

from application.views.member.views import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
