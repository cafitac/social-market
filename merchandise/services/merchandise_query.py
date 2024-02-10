from django.db.models import QuerySet
from rest_framework.serializers import ListSerializer

from merchandise.models import Merchandise
from merchandise.serializers import MerchandiseSerializer


class MerchandiseQueryService:

    @staticmethod
    def get_merchandises(user_id: int) -> MerchandiseSerializer:
        merchandises: QuerySet[Merchandise] = Merchandise.objects.filter(user_id=user_id)

        return MerchandiseSerializer(merchandises, many=True)
