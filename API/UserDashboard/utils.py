from API.UserDashboard.serializer import WalletDataSerializer
from LIB.utils import get_user_from_token
from Core.models import gold


def wallet_data(token_key):

    print(token_key)

    status, user, user_inf = get_user_from_token(token_key)

    if status:

        try:

            wallet_obj = gold.Wallet.objects.get(user=user)

        except:

            wallet_obj = gold.Wallet(

                user=user,
                gold_stock=0.0,
                money_stock=0.0

            )

            wallet_obj.save()

        wallet_serializer = WalletDataSerializer(data=[wallet_obj], many=True)
        wallet_serializer.is_valid()

        return {

            'wallet_gold_data': wallet_serializer.data[0]['gold_stock'],
            'wallet_money_data': wallet_serializer.data[0]['money_stock'],

        }, 200

    else:

        return {

            'response-en': 'wrong token',
            'response-fa': 'توکن معتبر نمیباشد'

        }, 400
