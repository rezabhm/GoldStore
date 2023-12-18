def change_status(data):

    for dt in data:

        if dt['request_status'] == 'accept':
            dt['request_status'] = 'تایید درخواست'

        elif dt['request_status'] == 'waiting':
            dt['request_status'] = 'در انتظار بررسی'

        else:
            dt['request_status'] = 'رد درخواست'

    return data
