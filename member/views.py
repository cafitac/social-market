from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from member.models import User


@login_required
def my_page(request):
    request_user: User = request.user
    return render(request, 'member/my-page.html', {
        'user': request_user,
    })
