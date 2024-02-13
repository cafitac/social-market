from typing import List

from django.db import models

from utils.model.base import AbstractBaseModel


class Merchandise(AbstractBaseModel):
    username = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    price = models.IntegerField(null=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'merchandise'
        verbose_name = "Merchandise"
        verbose_name_plural = f"{verbose_name} List"

    @staticmethod
    def create(username: str, name: str, description: str, price: int) -> 'Merchandise':
        return Merchandise(username=username, name=name, description=description, price=price)

    def is_owner(self, username: str):
        return self.username == username

    def update(self, update_data) -> List[str]:
        update_fields = []

        for field_name, value in update_data.items():
            update_fields.append(field_name)
            setattr(self, field_name, value)

        return update_fields

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
