from django.urls import path

from authenticate.views import login_form, logout_view

urlpatterns = [
    path("login/", login_form, name="login_form"),
    path('logout/', logout_view, name="logout_view"),
]
