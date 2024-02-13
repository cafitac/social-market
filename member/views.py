from django.shortcuts import render


def my_page(request):
    return render(request, 'member/my-page.html')
