from datetime import datetime

import pytz
from rest_framework.authtoken.serializers import AuthTokenSerializer


class CustomAuthTokenSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = data['user']
        user.last_login = datetime.utcnow().replace(tzinfo=pytz.utc)
        user.save()

        return data
