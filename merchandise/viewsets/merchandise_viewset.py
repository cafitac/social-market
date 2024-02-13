from typing import Optional

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from member.models import User
from merchandise.models import Merchandise
from merchandise.serializers.merchandise_create_serializer import MerchandiseCreateSerializer
from merchandise.serializers.merchandise_serializer import MerchandiseSerializer
from merchandise.serializers.merchandise_update_serializer import MerchandiseUpdateSerializer
from merchandise.serializers.stock_serializer import StockSerializer
from merchandise.serializers.stock_update_serializer import StockUpdateSerializer
from merchandise.services import MerchandiseCommandService, MerchandiseQueryService


class MerchandiseViewSet(viewsets.GenericViewSet):
    queryset = Merchandise.objects.filter(is_deleted=False)[:10]
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
        elif self.action == 'stock':
            if self.request.method == 'PATCH':
                self.serializer_class = StockUpdateSerializer

        return super().get_serializer(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        request_user: User = request.user

        q = request.GET.get("q", None)
        filter_type: str = request.GET.get("filter_type", None)
        username: str = request.GET.get("username", None)
        if q is not None:
            serializer: MerchandiseSerializer = self._get_list_by_q(request_user, q)
        elif filter_type is not None:
            serializer: MerchandiseSerializer = self._get_list_by_filter_type(request_user, filter_type, username)
        else:
            serializer: MerchandiseSerializer = MerchandiseQueryService.get_merchandises_response()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        request_user: User = request.user
        create_serializer: MerchandiseCreateSerializer = self.get_serializer(data=request.data)
        merchandise_id: int = MerchandiseCommandService.create(request_user.username, create_serializer)
        serializer: MerchandiseSerializer = MerchandiseQueryService.get_merchandise_response(merchandise_id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        serializer: MerchandiseSerializer = MerchandiseQueryService.get_merchandise_response(pk)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        request_user: User = request.user
        update_serializer: MerchandiseUpdateSerializer = self.get_serializer(data=request.data)
        merchandise_id: int = MerchandiseCommandService.update(request_user.username, pk, update_serializer)
        serializer: MerchandiseSerializer = MerchandiseQueryService.get_merchandise_response(merchandise_id)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        request_user: User = request.user
        MerchandiseCommandService.delete(request_user.username, pk)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get', 'patch'], url_path="stock")
    def stock(self, request, pk=None):
        request_user: User = request.user
        if request.method == 'GET':
            serializer: StockSerializer = MerchandiseQueryService.get_stock_response(pk)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PATCH':
            update_serializer: StockUpdateSerializer = self.get_serializer(data=request.data)
            merchandise_id: int = MerchandiseCommandService.update_stock(request_user.username, pk, update_serializer)
            serializer: StockSerializer = MerchandiseQueryService.get_stock_response(merchandise_id)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def _get_list_by_q(request_user: User, q: str) -> MerchandiseSerializer:
        return MerchandiseQueryService.get_merchandises_response_by_name(request_user.username, q)

    @staticmethod
    def _get_list_by_filter_type(request_user: User, filter_type: str, username: Optional[str]) -> MerchandiseSerializer:
        if filter_type == "own":
            return MerchandiseQueryService.get_merchandises_response_by_user_id(request_user.username)
        elif filter_type == 'user':
            if username is None:
                raise ValidationError("올바르지 않은 user_id입니다.")
            return MerchandiseQueryService.get_merchandises_response_by_user_id(username)
