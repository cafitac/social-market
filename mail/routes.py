from django.urls import path

from mail.views import check_active_code

urlpatterns = [
    path('active/<str:active_code>', check_active_code),
]
