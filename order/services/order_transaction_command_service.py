from order.models import Order, OrderTransaction


class OrderTransactionCommandService:

    @classmethod
    def create_order_transaction(cls, order: Order, total_price: int, payment_type: str) -> None:
        order_transaction: OrderTransaction = OrderTransaction.create(order, order.total_price(), payment_type)
        order_transaction.save()
