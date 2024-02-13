from rest_framework.exceptions import ValidationError

from member.models import Credit, User
from member.serializers.credit_serializer import CreditSerializer


class UserQueryService:

    @classmethod
    def get_user(cls, user_id: int):
        try:
            user: User = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise ValidationError("존재하지 않는 사용자입니다.")

        return user

    @classmethod
    def get_credit(cls, user_id: int) -> Credit:
        user: User = cls.get_user(user_id)

        return user.credit

    @classmethod
    def get_credit_response(cls, user_id: int) -> CreditSerializer:
        user: User = cls.get_user(user_id)

        return CreditSerializer(user.credit)
