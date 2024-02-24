from django.db import models

from order.models.order import Order
from utils.model.base import AbstractBaseModel


class OrderItem(AbstractBaseModel):
    order = models.ForeignKey(to=Order, related_name="order_items", on_delete=models.CASCADE, null=False)
    merchandise_id = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)

    class Meta:
        db_table = 'order_item'
        verbose_name = 'OrderItem'
        verbose_name_plural = f'{verbose_name} List'

    @classmethod
    def create(cls, order: Order, merchandise_id: int, price: int, amount: int) -> 'OrderItem':
        return cls(order=order, merchandise_id=merchandise_id, price=price, amount=amount)

    def calculate_item_total_price(self) -> int:
        return self.price * self.amount
