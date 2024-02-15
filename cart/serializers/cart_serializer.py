from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'merchandise_id', 'merchandise_name', 'merchandise_price', 'is_deleted', )
