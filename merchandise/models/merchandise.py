from django.db import models

from utils.model.base import AbstractBaseModel


class Merchandise(AbstractBaseModel):
    user_id = models.IntegerField(null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'merchandise'
        verbose_name = "Merchandise"
        verbose_name_plural = f"{verbose_name} List"

    @staticmethod
    def create(user_id: int, name: str, description: str, price: int) -> 'Merchandise':
        return Merchandise(user_id=user_id, name=name, description=description, price=price)
