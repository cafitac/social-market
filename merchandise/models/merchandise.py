from django.db import models

from utils.model.base import AbstractBaseModel


class Merchandise(AbstractBaseModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'merchandise'
        verbose_name = "Merchandise"
        verbose_name_plural = f"{verbose_name} List"
