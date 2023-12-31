from API.UserDashboard_DeskPage.serializer import WalletDataSerializer
from LIB.utils import get_user_from_token, check_wallet
from Core.models import gold


def wallet_data(token_key):

    status, user, user_inf = get_user_from_token(token_key)

    if status:
        try:
            name = f'{user.first_name}  {user.last_name}'
        except:
            name = ''

        wallet_obj = check_wallet(user)
        wallet_serializer = WalletDataSerializer(data=[wallet_obj], many=True)
        wallet_serializer.is_valid()

        return {

            'wallet_gold_data': round(wallet_serializer.data[0]['gold_stock'], 3),
            'wallet_money_data': wallet_serializer.data[0]['money_stock'],
            'name': name

        }, 200

    else:

        return {

            'responseEN': 'wrong token',
            'responseFA': 'توکن معتبر نمیباشد'

        }, 400
