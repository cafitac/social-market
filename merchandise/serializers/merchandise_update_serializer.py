from rest_framework import serializers


class MerchandiseUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_blank=False, required=False)
    description = serializers.CharField(max_length=500, allow_blank=True, required=False)
    price = serializers.IntegerField(allow_null=False, required=False)
