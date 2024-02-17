from merchandise.services import MerchandiseQueryService
from order.models import Order, OrderItem, OrderTransaction
from order.serializers.order_create_serializer import OrderCreateSerializer
from order.services.order_query_service import OrderQueryService


class OrderCommandService:

    @classmethod
    def create_order(cls, user_id: int, email: str, address: str) -> Order:
        order: Order = Order.create(user_id, email, address)
        order.save()

        return order

    @classmethod
    def paidOrder(cls, order_id: int):
        order: Order = OrderQueryService.get_order(order_id)
        order.paid()
