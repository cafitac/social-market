from typing import List

from rest_framework.exceptions import PermissionDenied

from merchandise.models import Merchandise, Stock
from merchandise.serializers import MerchandiseCreateSerializer, MerchandiseSerializer
from merchandise.serializers.merchandise_update_serializer import MerchandiseUpdateSerializer
from merchandise.services import MerchandiseQueryService


class MerchandiseCommandService:

    @staticmethod
    def create(username: str, create_serializer: MerchandiseCreateSerializer) -> int:
        create_serializer.is_valid(raise_exception=True)
        merchandise: Merchandise = Merchandise.create(
            username,
            create_serializer.validated_data['name'],
            create_serializer.validated_data['description'],
            create_serializer.validated_data['price']
        )
        merchandise.save()

        stock: Stock = Stock.create(merchandise=merchandise)
        stock.save()

        return merchandise.id

    @staticmethod
    def update(username: str, pk: int, update_serializer: MerchandiseUpdateSerializer) -> int:
        update_serializer.is_valid(raise_exception=True)
        merchandise: Merchandise = MerchandiseQueryService.get_merchandise(pk)
        if not merchandise.is_owner(username):
            raise PermissionDenied("상품 정보를 수정할 수 있는 권한이 없습니다.")

        update_fields: List[str] = merchandise.update(update_serializer.validated_data)
        merchandise.save(update_fields=update_fields)

        return merchandise.id

    @staticmethod
    def delete(username: str, pk: int):
        merchandise: Merchandise = MerchandiseQueryService.get_merchandise(pk)
        if not merchandise.is_owner(username):
            raise PermissionDenied("상품을 삭제할 수 있는 권한이 없습니다.")

        merchandise.delete()
