from rest_framework import serializers


class MerchandiseCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_blank=False)
    description = serializers.CharField(max_length=500, allow_blank=True)
    price = serializers.IntegerField(allow_null=False)
