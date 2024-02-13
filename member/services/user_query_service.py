from rest_framework.exceptions import ValidationError

from member.models import User
from member.serializers.credit_serializer import CreditSerializer


class UserQueryService:

    @staticmethod
    def get_credit(user_id: int) -> CreditSerializer:
        try:
            user: User = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise ValidationError("존재하지 않는 사용자입니다.")

        return CreditSerializer(user.credit)
