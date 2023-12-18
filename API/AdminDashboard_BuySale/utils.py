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

        if dt['request_status'] == 'accept':
            dt['request_status'] = 'تایید درخواست'

        elif dt['request_status'] == 'waiting':
            dt['request_status'] = 'در انتظار بررسی'

        else:
            dt['request_status'] = 'رد درخواست'

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


def prove_sale_request(sale_request_id, request_status):

    try:

        sale_gold_obj = SaleGold.objects.get(pk=sale_request_id)
        wallet_obj = check_wallet(sale_gold_obj.user)

        if wallet_obj.gold_stock >= sale_gold_obj.gold_amount:

            sale_gold_obj.request_status = request_status
            sale_gold_obj.save()

            if request_status == 'تایید درخواست':
                wallet_obj.gold_stock = wallet_obj.gold_stock - sale_gold_obj.gold_amount
                wallet_obj.save()

            return {

                'responseEN': 'successfully ...',
                'responseFA': 'در خواست شما با موفقیت ثبت شد'

            }, 200

        else:

            sale_gold_obj.request_status = 'رد درخواست'
            sale_gold_obj.save()

            return {

                'responseEN': 'your request gold amount is higher than your wallet gold amount',
                'responseFA': 'میزان درخواست طلای داده شده توسط مشتری بیشتر از میزان موجودی کاربر میباشد'

            }, 400

    except:

        return {

            'responseEN': 'wrong request id',
            'responseFA': 'ایدی وارد شده اشتباه میباشد'

        }, 400
