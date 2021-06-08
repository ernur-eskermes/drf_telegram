from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)

    def validate_password(self, value):
        try:
            validate_password(value)
        except serializers.ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):
        instance = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name']
        )
        return instance

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
        )
