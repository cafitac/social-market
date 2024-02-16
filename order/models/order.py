from django.db import models

from utils.model.base import AbstractBaseModel


class Order(AbstractBaseModel):
    user_id = models.IntegerField(null=False)
    email = models.CharField(max_length=150, blank=False, null=False)
    address = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = f'{verbose_name} List'
