from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = f'{verbose_name} List'

    @classmethod
    def create(cls, username: str, password: str, email: str) -> User:
        return cls(username=username, password=make_password(password), email=email, is_active=False)
