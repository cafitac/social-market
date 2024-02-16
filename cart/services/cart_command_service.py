from typing import List

from rest_framework.exceptions import PermissionDenied

from cart.models import Cart
from cart.serializers.cart_create_serializer import CartCreateSerializer
from cart.serializers.cart_update_serializer import CartUpdateSerializer
from cart.services.cart_query_service import CartQueryService
from merchandise.models import Merchandise
from merchandise.services import MerchandiseQueryService


class CartCommandService:

    @classmethod
    def create_cart(cls, user_id: int, create_serializer: CartCreateSerializer) -> int:
        create_serializer.is_valid(raise_exception=True)

        merchandise: Merchandise = MerchandiseQueryService.get_merchandise(create_serializer.validated_data['merchandise_id'])
        cart: Cart = Cart.create(
            user_id=user_id,
            merchandise_id=merchandise.id,
            merchandise_name=merchandise.name,
            merchandise_price=merchandise.price,
            merchandise_is_deleted=merchandise.is_deleted,
            amount=create_serializer.validated_data['amount'],
        )
        cart.save()
        return cart.id

    @classmethod
    def update_cart(cls, user_id: int, cart_id: int, update_serializer: CartUpdateSerializer) -> int:
        update_serializer.is_valid(raise_exception=True)
        cart: Cart = CartQueryService.get_cart(cart_id)
        if not cart.is_owner(user_id):
            raise PermissionDenied("장바구니를 수정할 수 있는 권한이 없습니다.")

        update_fields: List[str] = cart.update(update_serializer.validated_data)
        cart.save(update_fields=update_fields)

        return cart.id

    @classmethod
    def delete_cart(cls, cart_id: int) -> None:
        cart: Cart = CartQueryService.get_cart(cart_id)
        cart.delete()
        cart.save(update_fields=["is_deleted"])
