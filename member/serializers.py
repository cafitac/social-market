from rest_framework import serializers

from member.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', )


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, allow_blank=False)
    password = serializers.CharField(max_length=30, allow_blank=False, style={
        'input_type': 'password',
    })
    re_password = serializers.CharField(max_length=30, allow_blank=False, style={
        'input_type': 'password',
    })
    email = serializers.EmailField(max_length=128, allow_blank=False)
