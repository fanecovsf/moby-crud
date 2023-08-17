from rest_framework.authentication import BaseAuthentication

from moby.settings import VIBRA_API_KEY

class APIAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.header.get('AuthenticationKey')

        if api_key == VIBRA_API_KEY:
            return ('static_api_key', None)
        
        else:
            return None