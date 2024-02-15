from rest_framework import serializers


class CartCreateSerializer(serializers.Serializer):
    merchandise_id = serializers.IntegerField(required=True, allow_null=False)
