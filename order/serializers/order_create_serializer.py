from rest_framework import serializers


class OrderItemCreateSerializer(serializers.Serializer):
    merchandise_id = serializers.IntegerField(required=True, allow_null=False)
    amount = serializers.IntegerField(required=True, allow_null=False)


class OrderCreateSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=150, required=True, allow_blank=False, allow_null=False)
    address = serializers.CharField(max_length=150, required=True, allow_blank=False, allow_null=False)
    order_items = OrderItemCreateSerializer(many=True)
    payment_type = serializers.CharField(max_length=10, required=True, allow_blank=False, allow_null=False)
