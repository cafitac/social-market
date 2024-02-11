from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from member.models import User
from merchandise.models import Merchandise
from merchandise.serializers import MerchandiseCreateSerializer, MerchandiseSerializer
from merchandise.serializers.merchandise_update_serializer import MerchandiseUpdateSerializer
from merchandise.services import MerchandiseCommandService, MerchandiseQueryService


class MerchandiseViewSet(viewsets.GenericViewSet):
    queryset = Merchandise.objects.all()[:10]
    lookup_field = "pk"

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticatedOrReadOnly, ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticatedOrReadOnly, ]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated, ]

        return super().get_permissions()

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            self.serializer_class = MerchandiseCreateSerializer
        elif self.action == 'list':
            self.serializer_class = MerchandiseSerializer
        elif self.action == 'partial_update':
            self.serializer_class = MerchandiseUpdateSerializer

        return super().get_serializer(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        request_user: User = request.user
        serializer: MerchandiseSerializer = MerchandiseQueryService.get_merchandises_response(request_user.id)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        request_user: User = request.user
        create_serializer: MerchandiseCreateSerializer = self.get_serializer(data=request.data)
        serializer: MerchandiseSerializer = MerchandiseCommandService.create(request_user.id, create_serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        serializer: MerchandiseSerializer = MerchandiseQueryService.get_merchandise_response(pk)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        request_user: User = request.user
        update_serializer: MerchandiseUpdateSerializer = self.get_serializer(data=request.data)
        serializer: MerchandiseSerializer = MerchandiseCommandService.update(request_user.id, pk, update_serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        request_user: User = request.user
        MerchandiseCommandService.delete(request_user.id, pk)

        return Response(status=status.HTTP_204_NO_CONTENT)
