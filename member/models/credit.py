from django.db import models

from member.models import User


class Credit(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=False)
    balance = models.IntegerField(default=0)

    class Meta:
        db_table = 'credit'
        verbose_name = 'Credit'
        verbose_name_plural = f'{verbose_name} List'

    @classmethod
    def create(cls, user: User) -> 'Credit':
        return cls(user=user)

    def charge(self, amount: int):
        self.balance += amount
        self.save()

    def use(self, amount: int):
        self.balance -= amount
        self.save()
