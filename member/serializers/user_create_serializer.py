from rest_framework import serializers


class UserCreateSerializer(serializers.Serializer):
    """
    사용자 생성 시리얼라이저
    """

    username = serializers.CharField(max_length=150, allow_blank=False)
    password = serializers.CharField(max_length=30, allow_blank=False, style={
        'input_type': 'password',
    })
    re_password = serializers.CharField(max_length=30, allow_blank=False, style={
        'input_type': 'password',
    })
    email = serializers.EmailField(max_length=128, allow_blank=False)
