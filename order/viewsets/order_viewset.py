from rest_framework import status, viewsets
from rest_framework.response import Response

from member.models import User
from order.serializers.order_create_serializer import OrderCreateSerializer
from order.serializers.order_serializer import OrderSerializer
from order.services.order_command_service import OrderCommandService
from order.services.order_query_service import OrderQueryService
from usecase.create_order import CreateOrderUseCase


class OrderViewSet(viewsets.GenericViewSet):

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            self.serializer_class = OrderCreateSerializer

        return super().get_serializer(*args, **kwargs)

    def create(self, request):
        request_user: User = request.user
        create_serializer: OrderCreateSerializer = self.get_serializer(data=request.data)
        serializer: OrderSerializer = CreateOrderUseCase.execute(request_user.id, create_serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
