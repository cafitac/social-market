from django.db import models

from utils.model.base import AbstractBaseModel


class Delivery(AbstractBaseModel):
    seller_id = models.IntegerField(null=False)
    order_id = models.IntegerField(null=False)
    status = models.CharField(max_length=10, blank=False, null=False)

    class Meta:
        db_table = 'delivery'
        verbose_name = 'Delivery'
        verbose_name_plural = f'{verbose_name} List'
