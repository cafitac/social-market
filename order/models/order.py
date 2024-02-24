from django.db import models

from utils.model.base import AbstractBaseModel


class Order(AbstractBaseModel):
    user_id = models.IntegerField(null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    address = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = f'{verbose_name} List'

    @classmethod
    def create(cls, user_id: int, email: str, address: str) -> 'Order':
        return cls(user_id=user_id, email=email, address=address)

    def total_price(self):
        return sum([x.calculate_item_total_price() for x in self.order_items.all()])

    def paid(self):
        self.order_transaction.status = "PAID"
        self.order_transaction.save()

    def is_owner(self, user_id: int):
        return self.user_id == user_id
