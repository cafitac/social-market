from rest_framework import status, viewsets
from rest_framework.response import Response

from domain.member.models import User
from domain.member.serializers import UserCreateSerializer, UserSerializer
from domain.member.services import UserCommandService


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()[:10]

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            self.serializer_class = UserCreateSerializer

        return super().get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        create_serializer: UserCreateSerializer = self.get_serializer(data=request.data)
        serializer: UserSerializer = UserCommandService().save_user(create_serializer)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
