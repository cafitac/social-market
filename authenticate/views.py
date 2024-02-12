import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import status

from django_project.views import index
from member.models import User


@require_http_methods(['POST'])
@csrf_exempt
def session_login(request):
    data = json.loads(request.body)
    user: User = authenticate(username=data['username'], password=data['password'])
    if user.check_password(data['password']) and user.is_active:
        request.session.set_expiry(86400)
        login(request, user)

    return redirect(index)


def login_form(request):
    return render(request, 'auth/login_form.html')


def logout_view(request):
    logout(request)
    return render(request, 'auth/logout.html')
