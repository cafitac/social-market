from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.shortcuts import render

from merchandise.models import Merchandise


@login_required
def my_merchandises(request):
    merchandises: QuerySet[Merchandise] = Merchandise.objects.filter(username=request.user.username, is_deleted=False)

    return render(request, 'merchandise/my-list.html', {
        'merchandises': merchandises,
    })


@login_required
def merchandise_form(request):
    return render(request, 'merchandise/form.html')
