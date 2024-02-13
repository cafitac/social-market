from django.db import transaction

from mail.services.mail_command_service import MailCommandService
from member.serializers import UserCreateSerializer, UserSerializer
from member.services.user_command_service import UserCommandService


class UserRegisterUseCase:
    """
    사용자 회원가입 로직
    """

    @staticmethod
    @transaction.atomic
    def execute(serializer: UserCreateSerializer) -> UserSerializer:
        user_serializer: UserSerializer = UserCommandService().save_user(serializer)
        MailCommandService.send_mail(user_serializer.data['id'], user_serializer.data['email'])

        return user_serializer
