from rest_framework.authentication import  TokenAuthentication, get_authorization_header
from django.utils.translation import gettext_lazy as _
from rest_framework import HTTP_HEADER_ENCODING, exceptions


class CustomTokenAuthentication(TokenAuthentication):

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth:
            return None

        if len(auth) == 0:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 1:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[0].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)
