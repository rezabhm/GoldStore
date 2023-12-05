from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from Core.models.user import UserInformation


def get_user_from_token(token_key):

    try:

        user_id = Token.objects.get(key=token_key).user_id
        user = User.objects.get(id=user_id)
        user_inf = UserInformation.objects.get(user=user)

        return True, user, user_inf

    except:

        return False, _, _
