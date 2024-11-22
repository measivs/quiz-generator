from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}
        fields=[
            'id',
            'username',
            'email',
            'password',
            'password_confirm'
        ]

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Passwords must match')
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
