from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(required=True, allow_null=False)
