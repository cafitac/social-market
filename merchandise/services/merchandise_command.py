from merchandise.models import Merchandise
from merchandise.serializers import MerchandiseCreateSerializer, MerchandiseSerializer


class MerchandiseCommandService:

    @staticmethod
    def create(user_id: int, merchandise_create_serializer: MerchandiseCreateSerializer) -> MerchandiseSerializer:
        merchandise_create_serializer.is_valid(raise_exception=True)
        merchandise: Merchandise = Merchandise.create(
            user_id,
            merchandise_create_serializer.validated_data['name'],
            merchandise_create_serializer.validated_data['description'],
            merchandise_create_serializer.validated_data['price']
        )
        merchandise.save()

        return MerchandiseSerializer(merchandise)
