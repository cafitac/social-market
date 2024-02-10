from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ListSerializer

from merchandise.models import Merchandise
from merchandise.serializers import MerchandiseSerializer


class MerchandiseQueryService:

    @staticmethod
    def get_merchandises(user_id: int) -> MerchandiseSerializer:
        merchandises: QuerySet[Merchandise] = Merchandise.objects.filter(user_id=user_id)

        return MerchandiseSerializer(merchandises, many=True)

    @staticmethod
    def get_merchandise(pk):
        try:
            merchandise: Merchandise = Merchandise.objects.get(pk=pk)
        except Merchandise.DoesNotExist:
            raise ValidationError("존재하지 않는 상품입니다.")

        return MerchandiseSerializer(merchandise)
