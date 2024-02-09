from rest_framework import serializers

from member.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    사용자 기본 시리얼라이저
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', )
