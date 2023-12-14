from django.contrib.auth.models import User

from Core.models.stock import SaleGold
from LIB.utils import check_wallet


def add_inf(data):

    for dt in data:

        user_obj = User.objects.get(pk=dt['user'])

        dt['first_name'] = user_obj.first_name
        dt['last_name'] = user_obj.last_name
        dt['phone_number'] = user_obj.username

        dt['sale_date'] = ' '.join(dt['sale_date'].replace('T', ' ').split(' '))

        dt['request_status'] = 'تایید شده' if dt['request_status'] else 'در انتظار تایید'

    return data


def add_inf_buy(data):
    for dt in data:
        user_obj = User.objects.get(pk=dt['user'])

        dt['first_name'] = user_obj.first_name
        dt['last_name'] = user_obj.last_name
        dt['phone_number'] = user_obj.username

        dt['buy_date'] = ' '.join(dt['buy_date'].replace('T', ' ').split(' '))

        dt['request_status'] = 'تایید شده' if dt['request_status'] else 'در انتظار تایید'

    return data


def prove_sale_request(sale_request_id):

    try:

        sale_gold_obj = SaleGold.objects.get(pk=sale_request_id)
        sale_gold_obj.request_status = True
        sale_gold_obj.save()

        wallet_obj = check_wallet(sale_gold_obj.user)
        wallet_obj.gold_stock = wallet_obj.gold_stock - sale_gold_obj.gold_amount
        wallet_obj.save()

        return {

            'responseEN': 'successfully ...',
            'responseFA': 'در خواست شما با موفقیت ثبت شد'

        }, 200

    except:

        return {

            'responseEN': 'successfully ...',
            'responseFA': 'در خواست شما با موفقیت ثبت شد'

        }, 400
