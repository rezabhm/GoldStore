from django.utils import timezone

from Core.models.request import MoneyGetRequest, GoldGetRequest
from LIB.utils import get_user_from_token, check_wallet


def get_request_money(token_key, money_amount):

    status, user, user_inf = get_user_from_token(token_key)

    if status:

        wallet_obj = check_wallet(user)

        if (wallet_obj.money_stock >= money_amount) and (money_amount > 0.0):

            mgt = MoneyGetRequest(

                user=user,
                request_date=timezone.now(),
                money_amount=money_amount,

            )

            mgt.save()

            return {}, 200

        else:

            return {

                'response-en': f'your request\'s money amount are higher than your wallet\'s money amount.'
                               f'  your wallet: {wallet_obj.money_stock}',
                'response-fa': 'میزان پول درخواستی بیشتر از مقدار موجودی کیف پول شماست . مقدار موجودی کیف پول : '
                               f'{wallet_obj.money_stock}',

            }, 400

    else:

        return {

            'response-en': 'user didn\'t found',
            'response-fa': 'کاربر یافت نشد',

        }, 400


def get_request_gold(token_key, gold_amount):
    status, user, user_inf = get_user_from_token(token_key)

    if status:

        wallet_obj = check_wallet(user)

        if (wallet_obj.gold_stock >= gold_amount) and (gold_amount > 0.0):

            mgt = GoldGetRequest(

                user=user,
                request_date=timezone.now(),
                gold_amount=gold_amount,

            )

            mgt.save()

            return {}, 200

        else:

            return {

                'response-en': f'your request\'s gold amount are higher than your wallet\'s gold amount.'
                               f'  your wallet: {wallet_obj.gold_stock}',
                'response-fa': 'میزان طلای درخواستی بیشتر از مقدار موجودی کیف پول شماست . مقدار موجودی کیف شما : '
                               f'{wallet_obj.gold_stock}',

            }, 400

    else:

        return {

            'response-en': 'user didn\'t found',
            'response-fa': 'کاربر یافت نشد',

        }, 400
