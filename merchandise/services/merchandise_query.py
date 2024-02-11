from django.db.models import Q, QuerySet
from rest_framework.exceptions import ValidationError

from merchandise.models import Merchandise
from merchandise.serializers import MerchandiseSerializer


class MerchandiseQueryService:

    @staticmethod
    def get_merchandises_response() -> MerchandiseSerializer:
        merchandises: QuerySet[Merchandise] = Merchandise.objects.all().values("id", "name", "description", "price")

        return MerchandiseSerializer(merchandises, many=True)

    @staticmethod
    def get_merchandises_response_by_user_id(user_id: int) -> MerchandiseSerializer:
        merchandises: QuerySet[Merchandise] = Merchandise.objects.filter(user_id=user_id)

        return MerchandiseSerializer(merchandises, many=True)

    @staticmethod
    def get_merchandises_response_by_name(user_id: int, name: str) -> MerchandiseSerializer:
        query = Merchandise.objects.filter(~Q(user_id=user_id), name__icontains=name)
        merchandises: QuerySet[Merchandise] = Merchandise.objects.filter(~Q(user_id=user_id), name__icontains=name)

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
