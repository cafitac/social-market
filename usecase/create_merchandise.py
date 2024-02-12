from django.db import transaction

from merchandise.models import Merchandise
from merchandise.serializers import MerchandiseCreateSerializer
from merchandise.services import MerchandiseCommandService, StockCommandService


class CreateMerchandiseUseCase:
    @staticmethod
    @transaction.atomic
    def execute(username: str, create_serializer: MerchandiseCreateSerializer) -> int:
        merchandise: Merchandise = MerchandiseCommandService.create(username, create_serializer)
        StockCommandService.create(merchandise)

        return merchandise.id
