from typing import List

from django.db import models

from utils.model.base import AbstractBaseModel


class Cart(AbstractBaseModel):
    user_id = models.IntegerField(null=False)
    merchandise_id = models.IntegerField(null=False)
    merchandise_name = models.CharField(max_length=150, blank=False, null=False)
    merchandise_price = models.IntegerField(null=False)
    merchandise_is_deleted = models.BooleanField(default=False)
    amount = models.IntegerField(null=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'cart'
        verbose_name = "Cart"
        verbose_name_plural = f"{verbose_name} List"

    @staticmethod
    def create(user_id: int, merchandise_id: int, merchandise_name: str, merchandise_price: int, amount: int,
               merchandise_is_deleted: bool) -> 'Cart':
        return Cart(
            user_id=user_id,
            merchandise_id=merchandise_id,
            merchandise_name=merchandise_name,
            merchandise_price=merchandise_price,
            merchandise_is_deleted=merchandise_is_deleted,
            amount=amount,
        )

    def is_owner(self, user_id: int):
        return self.user_id == user_id

    def update(self, update_data) -> List[str]:
        update_fields = []

        for field_name, value in update_data.items():
            update_fields.append(field_name)
            setattr(self, field_name, value)

        return update_fields

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
