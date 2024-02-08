from rest_framework.exceptions import ValidationError

from mail.models import UserActiveMail


class MailCommandService:

    @staticmethod
    def check_user_active_mail_is_valid_and_expired(user_active_mail: str) -> None:
        try:
            user_active_mail: UserActiveMail = UserActiveMail.objects.get(active_code=user_active_mail)
            user_active_mail.expired()
            user_active_mail.save()
        except UserActiveMail.DoesNotExist:
            raise ValidationError("인증 코드가 일치하지 않습니다.")
