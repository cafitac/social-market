from django.db.models import QuerySet
from django.shortcuts import render

from merchandise.models import Merchandise


def index(request):
    q: str = request.GET.get('q')
    merchandises: QuerySet[Merchandise] = Merchandise.objects.all()
    if q is not None:
        merchandises = merchandises.filter(name__icontains=q)

    return render(request, 'index.html', {
        'merchandises': merchandises,
    })
