from django.shortcuts import render


def login(request):
    return render(request, 'member/login.html')
