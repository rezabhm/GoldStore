from django.contrib.auth.models import User

from Core.models.request import MoneyGetRequest


def add_user_inf(data):

    for dt in data:

        user_obj = User.objects.get(pk=dt['user'])

        dt['first_name'] = user_obj.first_name
        dt['last_name'] = user_obj.last_name
        dt['phone_number'] = user_obj.username

        dt['request_date'] = dt['request_date'].replace('T', ' ').split(' ')

    return data


def prove_money_get_request(get_req_id):

    try:

        get_request_obj = MoneyGetRequest.objects.get(pk=get_request_id)
        get_request_obj.request_status = True
        get_request_obj.save()

        return {

            'response-en': 'successfully ...',
            'response-fa':'درخواست موفقیت آمیز بود'

        }, 200

    except:

        return {

            'response-en': 'wrong id',
            'response-fa': 'آیدی ارسال شده اشتباه میباشد'

        }


