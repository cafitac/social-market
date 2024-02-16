from merchandise.services import MerchandiseQueryService
from order.models import Order, OrderItem, OrderTransaction
from order.serializers.order_create_serializer import OrderCreateSerializer


class OrderCommandService:

    @classmethod
    def create_order(cls, user_id: int, email: str, address: str) -> Order:
        order: Order = Order.create(user_id, email, address)
        order.save()

        return order
