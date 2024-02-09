from rest_framework import status, viewsets
from rest_framework.response import Response

from member.models import User
from merchandise.models import Merchandise
from merchandise.serializers import MerchandiseCreateSerializer
from merchandise.services import MerchandiseCommandService


class MerchandiseViewSet(viewsets.GenericViewSet):
    queryset = Merchandise.objects.all()[:10]

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            self.serializer_class = MerchandiseCreateSerializer

        return super().get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        request_user: User = request.user
        merchandise_create_serializer: MerchandiseCreateSerializer = self.get_serializer(data=request.data)
        serializer = MerchandiseCommandService.create(request_user.id, merchandise_create_serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
