from django.db import transaction

from mail.services.mail_command_service import MailCommandService
from member.services.user_command_service import UserCommandService


class ActivateUserUseCase:
    """
    사용자 활성화 로직
    """

    @staticmethod
    @transaction.atomic
    def execute(active_code: str) -> None:
        user_id: int = MailCommandService.check_user_active_mail_is_valid_and_expired(active_code)
        UserCommandService.active_user(user_id)
