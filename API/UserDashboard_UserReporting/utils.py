from LIB.utils import cvt_date


def change_status(data):

    for dt in data:

        if dt['request_status'] == 'accept':
            dt['request_status'] = 'تایید درخواست'

        elif dt['request_status'] == 'waiting':
            dt['request_status'] = 'در انتظار بررسی'

        else:
            dt['request_status'] = 'رد درخواست'

    return data


def change_date_buy_gold(data):

    for dt in data:
        dt['buy_date'] = cvt_date(dt['buy_date'])

    return data


def change_date_sale_gold(data):
    for dt in data:
        dt['sale_date'] = cvt_date(dt['sale_date'])

    return data


def change_date_get_request(data):
    for dt in data:
        dt['request_date'] = cvt_date(dt['request_date'])

    return data


def change_date_transaction(data):
    for dt in data:
        dt['payment_date'] = cvt_date(dt['payment_date'])

    return data

