from typing import List

from rest_framework.exceptions import PermissionDenied

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
        if not merchandise.is_owner(user_id):
            raise PermissionDenied("상품 정보를 수정할 수 있는 권한이 없습니다.")

        update_fields: List[str] = merchandise.update(update_serializer.validated_data)
        merchandise.save(update_fields=update_fields)

        return MerchandiseSerializer(merchandise)

    @staticmethod
    def delete(pk: int):
        merchandise: Merchandise = MerchandiseQueryService.get_merchandise(pk)
        merchandise.delete()
