from rest_framework import authentication

from djoser.models import Token


class TokenAuthentication(authentication.TokenAuthentication):
    model = Token
