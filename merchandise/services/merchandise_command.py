from typing import List

from merchandise.models import Merchandise
from merchandise.serializers import MerchandiseCreateSerializer, MerchandiseSerializer
from merchandise.serializers.merchandise_update_serializer import MerchandiseUpdateSerializer
from merchandise.services import MerchandiseQueryService


class MerchandiseCommandService:

    @staticmethod
    def create(user_id: int, create_serializer: MerchandiseCreateSerializer) -> MerchandiseSerializer:
        create_serializer.is_valid(raise_exception=True)
        merchandise: Merchandise = Merchandise.create(
            user_id,
            create_serializer.validated_data['name'],
            create_serializer.validated_data['description'],
            create_serializer.validated_data['price']
        )
        merchandise.save()

        return MerchandiseSerializer(merchandise)

    @staticmethod
    def update(user_id: int, pk: int, update_serializer: MerchandiseUpdateSerializer) -> MerchandiseSerializer:
        update_serializer.is_valid(raise_exception=True)
        merchandise: Merchandise = MerchandiseQueryService.get_merchandise(pk)
        update_fields: List[str] = merchandise.update(update_serializer.validated_data)
        merchandise.save(update_fields=update_fields)

        return MerchandiseSerializer(merchandise)
