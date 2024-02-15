from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import Cart
from cart.serializers.cart_create_serializer import CartCreateSerializer
from cart.serializers.cart_serializer import CartSerializer
from cart.services.cart_command_service import CartCommandService
from cart.services.CartQueryService import CartQueryService
from member.models import User


class CartViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        request_user: User = self.request.user
        queryset = Cart.objects.filter(user_id=request_user.id, is_deleted=False)[:10]

        return queryset

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            self.serializer_class = CartCreateSerializer

        return super().get_serializer(*args, **kwargs)

    def create(self, request):
        request_user: User = request.user
        create_serializer: CartCreateSerializer = self.get_serializer(data=request.data)
        cart_id: int = CartCommandService.create_cart(request_user.id, create_serializer)
        serializer: CartSerializer = CartQueryService.get_cart(cart_id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)