import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.authtoken.models import Token

from member.models import User


@require_http_methods(['POST'])
@csrf_exempt
def session_login(request):
    data = json.loads(request.body)
    user: User = authenticate(username=data['username'], password=data['password'])
    if user.check_password(data['password']) and user.is_active:
        token, _ = Token.objects.get_or_create(user=user)
        request.session.set_expiry(86400)
        login(request, user)
    else:
        JsonResponse({'message': '올바르지 않은 사용자 정보입니다.'}, status=401)

    return JsonResponse({'token': token.key}, status=200)


def login_form(request):
    return render(request, 'auth/login_form.html')


def logout_view(request):
    logout(request)
    return render(request, 'auth/logout.html')
