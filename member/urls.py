from django.urls import path

from member.views import login

urlpatterns = [
    path("login/", login, name="login"),
]
