from time import time
from uuid import uuid4

from django.db import models

from utils.model.base import AbstractBaseModel


class UserActiveMail(AbstractBaseModel):
    """
    사용자에 대한 인증 메일의 활성화 상태를 관리
    """

    user_id = models.BigIntegerField(null=False, unique=True)
    active_code = models.CharField(max_length=128, null=False, unique=True)
    is_expired = models.BooleanField(default=False)

    class Meta:
        db_table = "user_active_mail"
        verbose_name = "User Active Mail"
        verbose_name_plural = f"{verbose_name} List"

    @classmethod
    def create(cls, user_id):
        active_code: str = str(uuid4()) + str(time())
        return cls(user_id=user_id, active_code=active_code)

    def expired(self):
        self.is_expired = True
