from django.db import transaction

from cart.services.cart_command_service import CartCommandService
from merchandise.services import MerchandiseCommandService


class DeleteMerchandiseUseCase:

    @classmethod
    @transaction.atomic
    def execute(cls, username: str, merchandise_id: int):
        merchandise_id: int = MerchandiseCommandService.delete(username, merchandise_id)
        CartCommandService.update_merchandise_is_deleted(merchandise_id)
