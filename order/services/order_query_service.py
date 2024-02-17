from rest_framework.exceptions import ValidationError

from order.models import Order
from order.serializers.order_serializer import OrderSerializer


class OrderQueryService:

    @classmethod
    def get_order(cls, order_id: int) -> Order:
        try:
            order: Order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            raise ValidationError("존재하지 않는 주문 정보입니다.")

        return order

    @classmethod
    def get_order_response(cls, order_id) -> OrderSerializer:
        try:
            order: Order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            raise ValidationError("존재하지 않는 주문 정보입니다.")

        return OrderSerializer(order)
