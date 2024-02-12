from django.db import models

from utils.model.base import AbstractBaseModel


class Stock(AbstractBaseModel):
    merchandise_id = models.IntegerField(null=False)
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'stock'
        verbose_name = 'Stock'
        verbose_name_plural = f'{verbose_name} List'
