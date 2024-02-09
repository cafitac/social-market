from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from usecase.active_user import ActivateUserUseCase


@require_http_methods(["GET"])
def check_active_code(request, active_code: str):
    ActivateUserUseCase.execute(active_code=active_code)

    return HttpResponse("인증되었습니다.", status=200)
