from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from member.models import User
from member.serializers import UserCreateSerializer, UserSerializer
from member.serializers.credit_serializer import CreditSerializer
from member.serializers.update_credit_serializer import UpdateCreditSerializer
from member.services.user_command_service import UserCommandService
from member.services.user_query_service import UserQueryService
from usecase.user_register import UserRegisterUseCase


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()[:10]

    def get_permissions(self):
        if self.action == 'credit':
            self.permission_classes = (IsAuthenticated, )

        return super().get_permissions()

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            self.serializer_class = UserCreateSerializer
        elif self.action == 'credit':
            if self.request.method == 'POST':
                self.serializer_class = UpdateCreditSerializer

        return super().get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        create_serializer: UserCreateSerializer = self.get_serializer(data=request.data)
        serializer: UserSerializer = UserRegisterUseCase.execute(create_serializer)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get', 'post'], url_path="credit")
    def credit(self, request):
        request_user: User = request.user
        if request.method == 'GET':
            serializer: CreditSerializer = UserQueryService.get_credit_response(request_user.id)

            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            update_serializer: UpdateCreditSerializer = self.get_serializer(data=request.data)
            user_id: int = UserCommandService.charge_credit(request_user.id, update_serializer)
            serializer: CreditSerializer = UserQueryService.get_credit_response(user_id)

            return Response(serializer.data, status=status.HTTP_200_OK)
