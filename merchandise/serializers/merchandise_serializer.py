from rest_framework import serializers

from merchandise.models import Merchandise


class MerchandiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Merchandise
        fields = ["id", "name", "description", "price", ]
