from rest_framework import serializers

from merchandise.models import Stock


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ['count', ]
