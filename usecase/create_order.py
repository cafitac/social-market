from django.db import transaction

from merchandise.models import Merchandise
from merchandise.services import MerchandiseQueryService
from order.models import Order, OrderItem
from order.serializers.order_create_serializer import OrderCreateSerializer
from order.serializers.order_serializer import OrderSerializer
from order.services.order_command_service import OrderCommandService
from order.services.order_item_command_service import OrderItemCommandService
from order.services.order_transaction_command_service import OrderTransactionCommandService


class CreateOrderUseCase:

    @classmethod
    @transaction.atomic
    def execute(cls, user_id: int, create_serializer: OrderCreateSerializer) -> OrderSerializer:
        create_serializer.is_valid(raise_exception=True)
        data = create_serializer.validated_data
        order: Order = OrderCommandService.create_order(user_id, data['email'], data['address'])

        for order_item_serializer in data['order_items']:
            merchandise_id = order_item_serializer['merchandise_id']
            merchandise: Merchandise = MerchandiseQueryService.get_merchandise(merchandise_id)
            OrderItemCommandService.create_order_item(
                order,
                merchandise.id,
                merchandise.price,
                order_item_serializer['amount']
            )

        OrderTransactionCommandService.create_order_transaction(order, order.total_price(), data['payment_type'])

        return OrderSerializer(order)
