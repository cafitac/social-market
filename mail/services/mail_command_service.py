from django.conf import settings
from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError

from mail.models import UserActiveMail


class MailCommandService:

    @staticmethod
    def send_mail(user_id: int, to: str):
        user_active_mail = UserActiveMail.create(user_id=user_id)
        user_active_mail.save()

        send_mail(
            "[Social Market] 본인 인증 메일",
            f"http://localhost:8000/api/mail/active/{user_active_mail.active_code}",
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently=False,
        )

    @staticmethod
    def check_user_active_mail_is_valid_and_expired(user_active_mail: str) -> int:
        try:
            user_active_mail: UserActiveMail = UserActiveMail.objects.get(active_code=user_active_mail)
            user_active_mail.expired()
            user_active_mail.save()
        except UserActiveMail.DoesNotExist:
            raise ValidationError("인증 코드가 일치하지 않습니다.")

        return user_active_mail.user_id
