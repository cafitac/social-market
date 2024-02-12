from django.db.models import QuerySet
from django.shortcuts import render

from merchandise.models import Merchandise


def index(request):
    merchandises: QuerySet[Merchandise] = Merchandise.objects.all()
    return render(request, 'index.html', {
        'merchandises': merchandises,
    })
