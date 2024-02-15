from rest_framework.exceptions import ValidationError

from cart.models import Cart
from cart.serializers.cart_serializer import CartSerializer


class CartQueryService:

    @classmethod
    def get_cart(cls, cart_id: int) -> CartSerializer:
        try:
            cart: Cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:
            raise ValidationError("존재하지 않는 장바구니 정보입니다.")

        return CartSerializer(cart)
