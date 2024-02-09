from django.db import transaction

from mail.services.mail_command_service import MailCommandService
from member.serializers import UserCreateSerializer, UserSerializer
from member.services import UserCommandService


class UserRegisterUseCase:

    @staticmethod
    @transaction.atomic
    def execute(serializer: UserCreateSerializer) -> UserSerializer:
        user_serializer: UserSerializer = UserCommandService().save_user(serializer)
        MailCommandService.send_mail(user_serializer.data['id'], user_serializer.data['email'])

        return user_serializer
