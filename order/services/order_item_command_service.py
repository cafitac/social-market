from order.models import Order, OrderItem


class OrderItemCommandService:

    @classmethod
    def create_order_item(cls, order: Order, merchandise_id: int, price: int, amount: int) -> None:
        order_item: OrderItem = OrderItem.create(order=order, merchandise_id=merchandise_id, price=price, amount=amount)
        order_item.save()
