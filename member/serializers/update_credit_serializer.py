from rest_framework import serializers


class UpdateCreditSerializer(serializers.Serializer):
    charge_amount = serializers.IntegerField(allow_null=False)
