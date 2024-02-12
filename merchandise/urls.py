from django.urls import path

from merchandise.views import merchandise_form, my_merchandises

urlpatterns = [
    path('my-merchandises', my_merchandises, name="my-merchandises"),
    path('merchandise-form', merchandise_form, name="merchandise_form"),
]
