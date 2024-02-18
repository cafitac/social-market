from django.db.models import Q, QuerySet
from django.shortcuts import render

from merchandise.models import Merchandise


def index(request):
    q: str = request.GET.get('q')
    merchandises: QuerySet[Merchandise] = Merchandise.objects.filter(is_deleted=False)

    if request.user is not None:
        merchandises: QuerySet[Merchandise] = merchandises.filter(~Q(username=request.user))

    if q is not None:
        merchandises: QuerySet[Merchandise] = merchandises.filter(name__icontains=q)

    return render(request, 'index.html', {
        'merchandises': merchandises,
    })
