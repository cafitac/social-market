from django.urls import path

from member.views import my_page

urlpatterns = [
    path('my-page', my_page, name='my-page'),
]
