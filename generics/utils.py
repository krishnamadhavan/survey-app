from djoser.models import Token


class ActionViewMixin(object):
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self._action(serializer)


def login_user(user, serializer_data=None):
    serializer_data = serializer_data or {}
    token_data = dict((k, v) for k, v in serializer_data.items() if k in Token.LOGIN_FIELDS)
    token, _ = Token.objects.get_or_create(user=user, **token_data)
    return token
