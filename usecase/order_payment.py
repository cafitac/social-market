from django.db import transaction

from member.models import User
from member.services.user_command_service import UserCommandService
from member.services.user_query_service import UserQueryService
from merchandise.services import MerchandiseCommandService
from order.models import Order
from order.serializers.order_serializer import OrderSerializer
from order.serializers.payment_serializer import PaymentSerializer
from order.services.order_command_service import OrderCommandService
from order.services.order_query_service import OrderQueryService


class OrderPaymentUseCase:

    @classmethod
    @transaction.atomic
    def execute(cls, user_id: int, payment_serializer: PaymentSerializer) -> OrderSerializer:
        payment_serializer.is_valid(raise_exception=True)
        order: Order = OrderQueryService.get_order(payment_serializer.validated_data['order_id'])

        UserCommandService.use_credit(user_id, order.total_price())

        order_items = order.order_items.all()
        MerchandiseCommandService.decrease_stock([{
            "merchandise_id": order_item.merchandise_id,
            "amount": order_item.amount
        } for order_item in order_items])

        order: Order = OrderCommandService.paidOrder(payment_serializer.validated_data['order_id'])

        return OrderSerializer(order)
