from django.contrib.auth.models import User


def add_user_inf(data):

    for dt in data:

        user_obj = User.objects.get(pk=dt['user'])

        dt['first_name'] = user_obj.first_name
        dt['last_name'] = user_obj.last_name
        dt['phone_number'] = user_obj.username
        dt['payment_date'] = ' '.join(dt['payment_date'].replace('T', ' ').split(' '))

    return data
