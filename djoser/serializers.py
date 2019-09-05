from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from djoser import models, constants

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=6, max_length=15)
    uuid = serializers.CharField()

    default_error_messages = {
        'invalid_credentials': constants.INVALID_CREDENTIALS,
        'invalid_superuser': constants.INVALID_SUPERUSER,
        'inactive_account': constants.INACTIVE_ACCOUNT,
    }

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate_username(self, username):
        try:
            self.user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            self.user = None

        if not self.user:
            self.fail('invalid_superuser')

        if not self.user.is_active:
            self.fail('inactive_account')

        return username

    def validate(self, attrs):
        if not self.user.check_password(attrs['password']):
            self.fail('invalid_credentials')

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'email', 'date_joined', 'is_active')


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = models.Token
        fields = ('user', 'auth_token')
