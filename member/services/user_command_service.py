from rest_framework.exceptions import ValidationError

from member.models import Credit, User
from member.serializers import UserCreateSerializer, UserSerializer
from member.serializers.update_credit_serializer import UpdateCreditSerializer
from member.services.user_query_service import UserQueryService


class UserCommandService:

    def save_user(self, serializer: UserCreateSerializer) -> UserSerializer:
        serializer.is_valid(raise_exception=True)
        self._check_before_save_user(serializer)

        user: User = User.create(serializer.validated_data['username'],
                                 serializer.validated_data['password'],
                                 serializer.validated_data['email'])
        user.save()

        return UserSerializer(user)

    @staticmethod
    def active_user(user_id):
        try:
            user: User = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise ValidationError("존재하지 않는 사용자입니다.")

        user.is_active = True
        user.save()

    @classmethod
    def charge_credit(cls, user_id: int, update_serializer: UpdateCreditSerializer) -> int:
        update_serializer.is_valid(raise_exception=True)

        credit: Credit = UserQueryService.get_credit(user_id)
        credit.charge(update_serializer.validated_data['charge_amount'])
        credit.save()

        return user_id

    def _check_before_save_user(self, serializer: UserCreateSerializer):
        self._check_username_is_exists(serializer.validated_data['username'])
        self._check_password_and_re_password_is_same(serializer.validated_data['password'],
                                                     serializer.validated_data['re_password'])

    @staticmethod
    def _check_username_is_exists(username: str):
        if User.objects.filter(username=username).exists():
            raise ValidationError("이미 사용 중인 아이디입니다.")

    @staticmethod
    def _check_password_and_re_password_is_same(password: str, re_password: str) -> None:
        if not password == re_password:
            raise ValidationError("비밀번호가 일치하지 않습니다.")
