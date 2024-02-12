from django.urls import path
from rest_framework.authtoken import views

from authenticate.views import session_login

urlpatterns = [
    path('token', views.obtain_auth_token),
    path('session/login', session_login),
]
