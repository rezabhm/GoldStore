from django.contrib.auth.models import User

from Core.models.request import MoneyGetRequest, GoldGetRequest
from LIB.utils import check_wallet


def add_user_inf(data):

    for dt in data:

        user_obj = User.objects.get(pk=dt['user'])

        dt['first_name'] = user_obj.first_name
        dt['last_name'] = user_obj.last_name
        dt['phone_number'] = user_obj.username

        dt['request_date'] = ' '.join(dt['request_date'].replace('T', ' ').split(' '))
        # dt['request_status'] = 'تایید شده' if dt['request_status'] else 'در انتظار تایید'

    return data


def prove_money_get_request(get_req_id, request_type):

    try:

        get_request_obj = MoneyGetRequest.objects.get(pk=get_req_id)
        wallet_obj = check_wallet(get_request_obj.user)

        if get_request_obj.money_amount <= wallet_obj.money_stock:

            get_request_obj.request_status = request_type
            get_request_obj.save()

            if request_type == 'تایید درخواست':

                wallet_obj.money_stock = wallet_obj.money_stock - get_request_obj.money_amount
                wallet_obj.save()

            return {

                'responseEN': 'successfully ...',
                'responseFA': 'درخواست موفقیت آمیز بود'

            }, 200

        else:

            get_request_obj.request_status = 'رد درخواست'
            get_request_obj.save()

            return {

                'responseEN': 'users requests money amount are higher than users wallet money amount',
                'responseFA': 'میزان پول درخواستی توسط مشتری بیشتر از مقدار کیف پول مشتری است'

            }, 400

    except:

        return {

            'responseEN': 'wrong id',
            'responseFA': 'آیدی ارسال شده اشتباه میباشد'

        }, 400


def prove_gold_get_request(get_req_id, request_type):

    try:

        get_request_obj = GoldGetRequest.objects.get(pk=get_req_id)
        wallet_obj = check_wallet(get_request_obj.user)

        if get_request_obj.gold_amount <= wallet_obj.gold_stock:

            get_request_obj.request_status = request_type
            get_request_obj.save()

            if request_type == 'تایید درخواست':

                wallet_obj.gold_stock = wallet_obj.gold_stock - get_request_obj.gold_amount
                wallet_obj.save()

            return {

                'responseEN': 'successfully ...',
                'responseFA': 'درخواست موفقیت آمیز بود'

            }, 200

        else:

            get_request_obj.request_status = 'رد درخواست'
            get_request_obj.save()

            return {

                'responseEN': 'users requests money amount are higher than users wallet money amount',
                'responseFA': 'میزان طلای درخواستی توسط مشتری بیشتر از مقدار طلای موجود در کیف پول مشتری است'

            }, 400


    except:

        return {

            'responseEN': 'wrong id',
            'responseFA': 'آیدی ارسال شده اشتباه میباشد'

        }, 400
