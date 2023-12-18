import jdatetime
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from Core.models import gold
from Core.models.user import UserInformation


def get_user_from_token(token_key):

    try:

        user_id = Token.objects.get(key=token_key).user_id
        user = User.objects.get(id=user_id)
        user_inf = UserInformation.objects.get(user=user)

        return True, user, user_inf

    except:

        return False, None, None


def check_wallet(user):

    try:

        wallet_obj = gold.Wallet.objects.get(user=user)

    except:

        wallet_obj = gold.Wallet(

            user=user,
            gold_stock=0.0,
            money_stock=0.0

        )

        wallet_obj.save()

    return wallet_obj


def cvt_date(x):

    time = ' '.join(':'.join('T'.join(x.replace('T', ' ').split(' ')).split(':')[:2]).replace('T', ' ').split(
        ' ')).replace('-', '/')

    time_2 = time.split(' ')
    date = time_2[0].split('/')

    date = jdatetime.date.fromgregorian(year=int(date[0]), month=int(date[1]), day=int(date[2]))

    return f'{date.year}/{date.month}/{date.day} {time_2[1]}'
