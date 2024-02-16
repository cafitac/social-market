from rest_framework import serializers


class CartUpdateSerializer(serializers.Serializer):
    amount = serializers.IntegerField(allow_null=False)
