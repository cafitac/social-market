from rest_framework import serializers

from member.models import Credit


class CreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credit
        fields = ['balance', ]
