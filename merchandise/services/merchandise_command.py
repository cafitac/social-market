from typing import List

from rest_framework.exceptions import PermissionDenied

from merchandise.models import Merchandise, Stock
from merchandise.serializers.merchandise_create_serializer import MerchandiseCreateSerializer
from merchandise.serializers.merchandise_update_serializer import MerchandiseUpdateSerializer
from merchandise.serializers.stock_serializer import StockSerializer
from merchandise.serializers.stock_update_serializer import StockUpdateSerializer
from merchandise.services.merchandise_query import MerchandiseQueryService
from utils.exceptions.unprocessable_error import UnprocessableError


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
    def delete(username: str, pk: int) -> int:
        merchandise: Merchandise = MerchandiseQueryService.get_merchandise(pk)
        if not merchandise.is_owner(username):
            raise PermissionDenied("상품을 삭제할 수 있는 권한이 없습니다.")

        merchandise.delete()
        merchandise.save()

        return merchandise.id

    @staticmethod
    def update_stock(username, merchandise_id: int, update_serializer: StockUpdateSerializer) -> int:
        update_serializer.is_valid(raise_exception=True)
        merchandise: Merchandise = MerchandiseQueryService.get_merchandise(merchandise_id)
        if not merchandise.is_owner(username):
            raise PermissionDenied("상품 재고를 수정할 수 있는 권한이 없습니다.")

        merchandise.stock.update_count(update_serializer.validated_data['count'])

        merchandise.stock.save(update_fields=['count'])

        return merchandise.id

    @classmethod
    def decrease_stock(cls, amount_datas: List[dict]) -> None:
        for amount_data in amount_datas:
            stock: Stock = MerchandiseQueryService.get_stock(amount_data['merchandise_id'])

            if amount_data['amount'] > stock.count:
                raise UnprocessableError("상품 재고가 부족합니다.")

            stock.decrease(amount_data['amount'])
