from django.db.models import Q, QuerySet
from rest_framework.exceptions import ValidationError

from merchandise.models import Merchandise, Stock
from merchandise.serializers.merchandise_serializer import MerchandiseSerializer
from merchandise.serializers.stock_serializer import StockSerializer


class MerchandiseQueryService:

    @staticmethod
    def get_merchandises_response() -> MerchandiseSerializer:
        merchandises: QuerySet[Merchandise] = Merchandise.objects.filter(is_deleted=False).values("id", "name", "description", "price")

        return MerchandiseSerializer(merchandises, many=True)

    @staticmethod
    def get_merchandises_response_by_user_id(username: str) -> MerchandiseSerializer:
        merchandises: QuerySet[Merchandise] = Merchandise.objects.filter(username=username)

        return MerchandiseSerializer(merchandises, many=True)

    @staticmethod
    def get_merchandises_response_by_name(username: str, name: str) -> MerchandiseSerializer:
        query = Merchandise.objects.filter(~Q(username=username), name__icontains=name)
        merchandises: QuerySet[Merchandise] = Merchandise.objects.filter(~Q(username=username), name__icontains=name)

        return MerchandiseSerializer(merchandises, many=True)

    @staticmethod
    def get_merchandise(pk: int) -> Merchandise:
        try:
            merchandise: Merchandise = Merchandise.objects.get(pk=pk)
        except Merchandise.DoesNotExist:
            raise ValidationError("존재하지 않는 상품입니다.")

        return merchandise

    @staticmethod
    def get_merchandise_response(pk: int):
        try:
            merchandise: Merchandise = Merchandise.objects.get(pk=pk)
        except Merchandise.DoesNotExist:
            raise ValidationError("존재하지 않는 상품입니다.")

        return MerchandiseSerializer(merchandise)

    @classmethod
    def get_stock(cls, merchandise_id: int) -> Stock:
        try:
            merchandise: Merchandise = Merchandise.objects.get(pk=merchandise_id)
        except Merchandise.DoesNotExist:
            raise ValidationError("존재하지 않는 상품입니다.")

        return merchandise.stock

    @classmethod
    def get_stock_response(cls, merchandise_id: int) -> StockSerializer:
        try:
            merchandise: Merchandise = Merchandise.objects.get(pk=merchandise_id)
        except Merchandise.DoesNotExist:
            raise ValidationError("존재하지 않는 상품입니다.")

        return StockSerializer(merchandise.stock)
