from rest_framework import serializers


class StockUpdateSerializer(serializers.Serializer):
    count = serializers.IntegerField(allow_null=False)
