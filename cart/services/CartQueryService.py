from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError

from cart.models import Cart
from cart.serializers.cart_serializer import CartSerializer


class CartQueryService:

    @classmethod
    def get_cart_response(cls, cart_id: int) -> CartSerializer:
        try:
            cart: Cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:
            raise ValidationError("존재하지 않는 장바구니 정보입니다.")

        return CartSerializer(cart)

    @classmethod
    def get_carts_response(cls, user_id: int) -> CartSerializer:
        carts: QuerySet[Cart] = Cart.objects.filter(user_id=user_id, is_deleted=False)

        return CartSerializer(carts, many=True)
