from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from member.models import User
from order.serializers.order_create_serializer import OrderCreateSerializer
from order.serializers.order_serializer import OrderSerializer
from order.serializers.payment_serializer import PaymentSerializer
from usecase.create_order import CreateOrderUseCase
from usecase.order_payment import OrderPaymentUseCase


class OrderViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            self.serializer_class = OrderCreateSerializer
        elif self.action == 'payment':
            self.serializer_class = PaymentSerializer

        return super().get_serializer(*args, **kwargs)

    def create(self, request):
        request_user: User = request.user
        create_serializer: OrderCreateSerializer = self.get_serializer(data=request.data)
        serializer: OrderSerializer = CreateOrderUseCase.execute(request_user.id, create_serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False, url_path="payment")
    def payment(self, request):
        request_user: User = request.user
        payment_serializer: PaymentSerializer = self.get_serializer(data=request.data)
        serializer: OrderSerializer = OrderPaymentUseCase.execute(request_user.id, payment_serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
