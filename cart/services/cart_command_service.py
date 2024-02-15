from cart.models import Cart
from cart.serializers.cart_create_serializer import CartCreateSerializer
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
        )
        cart.save()
        return cart.id
