from django.db import models

from utils.model.base import AbstractBaseModel


class Cart(AbstractBaseModel):
    user_id = models.IntegerField(null=False)
    merchandise_id = models.IntegerField(null=False)
    merchandise_name = models.CharField(max_length=150, blank=False, null=False)
    merchandise_price = models.IntegerField(null=False)
    merchandise_is_deleted = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'cart'
        verbose_name = "Cart"
        verbose_name_plural = f"{verbose_name} List"

    @staticmethod
    def create(user_id: int, merchandise_id: int, merchandise_name: str, merchandise_price: int,
               merchandise_is_deleted: bool) -> 'Cart':
        return Cart(
            user_id=user_id,
            merchandise_id=merchandise_id,
            merchandise_name=merchandise_name,
            merchandise_price=merchandise_price,
            merchandise_is_deleted=merchandise_is_deleted,
        )
