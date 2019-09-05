from django.contrib.auth import login, logout
from rest_framework import generics, response, status, permissions

from djoser import serializers
from generics.utils import ActionViewMixin, login_user


class LoginView(ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to login an user (create authentication token).
    """
    serializer_class = serializers.LoginSerializer
    token_serializer_class = serializers.TokenSerializer

    def _action(self, serializer, *args, **kwargs):
        login(
            self.request, serializer.user, *args, **kwargs
        )
        token = login_user(serializer.user, serializer.data)
        return response.Response(
            data=self.token_serializer_class(token).data,
            status=status.HTTP_200_OK,
        )


class LogoutView(generics.GenericAPIView):
    """
    Use this endpoint to logout an user (destroy authentication token).
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request):
        if self.request.auth:
            request.auth.delete()
            logout(request)
        return response.Response(status=status.HTTP_200_OK)
