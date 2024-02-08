from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from mail.services.mail_command_service import MailCommandService


@require_http_methods(["GET"])
def check_active_code(request, active_code: str):
    MailCommandService.check_user_active_mail_is_valid_and_expired(active_code)

    return HttpResponse("인증되었습니다.", status=200)
