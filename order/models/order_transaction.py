from django.db import models

from order.models.order import Order
from utils.model.base import AbstractBaseModel


class OrderTransaction(AbstractBaseModel):
    order = models.OneToOneField(to=Order, related_name='order_transaction', on_delete=models.CASCADE, null=False)
    # transaction_uid 가 나중에 PG 사를 붙이면 필요해질 예정
    total_price = models.IntegerField(null=False)
    payment_type = models.CharField(max_length=10, null=False)
    status = models.CharField(max_length=10, null=False)

    class Meta:
        db_table = 'order_transaction'
        verbose_name = 'OrderTransaction'
        verbose_name_plural = f'{verbose_name} List'
