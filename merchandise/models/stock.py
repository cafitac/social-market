from django.db import models

from merchandise.models import Merchandise
from utils.model.base import AbstractBaseModel


class Stock(AbstractBaseModel):
    merchandise = models.OneToOneField(to=Merchandise, on_delete=models.CASCADE, null=False)
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'stock'
        verbose_name = 'Stock'
        verbose_name_plural = f'{verbose_name} List'

    @staticmethod
    def create(merchandise: Merchandise) -> 'Stock':
        return Stock(merchandise=merchandise)

    def update_count(self, stock_count):
        self.count = stock_count

    def decrease(self, amount):
        self.count -= amount
        self.save()
