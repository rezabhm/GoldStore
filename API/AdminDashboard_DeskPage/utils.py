from django.contrib.auth.models import User

from API.AdminDashboard_DeskPage.serializer import UsersInformationListSerializer
from Core.models.gold import Wallet


def user_information_list():

    user_list = User.objects.all()
    user_serializer = UsersInformationListSerializer(data=user_list, many=True)
    user_serializer.is_valid()
    data = user_serializer.data

    for dt in data:

        try:

            wallet_obj = Wallet.objects.get(user__username=dt['username'])
            dt['money_amount'] = wallet_obj.money_stock
            dt['gold_amount'] = wallet_obj.gold_stock

        except:

            wallet_obj = Wallet(

                user=User.objects.get(username=dt['username']),
                money_stock=0.0,
                gold_stock=0.0

            )

            wallet_obj.save()

            dt['money_amount'] = wallet_obj.money_stock
            dt['gold_amount'] = wallet_obj.gold_stock

        dt['phone_number'] = dt['username']

    return {

        'data': data

    }


def user_change_gold_amount(data):

    try:

        user_obj = User.objects.get(username=data['phone_number'])

    except:

        return {

            'responseEN': 'user with this phone number didn\'t found',
            'responseFA': 'کاربر با این شماره تلفن یافت نشد'

        }, 404

    try:

        wallet_obj = Wallet.objects.get(user=user_obj)
        wallet_obj.gold_stock = data['gold_amount']
        wallet_obj.save()

    except:

        wallet_obj = Wallet(

            user=user_obj,
            gold_stock=data['gold_amount'],
            money_stock=0.0

        )
        wallet_obj.save()

    return {

        'responseEN': 'successfully change ...',
        'responseFA': 'تغییرات با موفقیت اعمال شد',

    }, 200


def user_change_money_amount(data):

    try:

        user_obj = User.objects.get(username=data['phone_number'])

    except:

        return {

            'responseEN': 'user with this phone number didn\'t found',
            'responseFA': 'کاربر با این شماره تلفن یافت نشد'

        }, 404

    try:

        wallet_obj = Wallet.objects.get(user=user_obj)
        wallet_obj.money_stock = data['money_amount']
        wallet_obj.save()

    except:

        wallet_obj = Wallet(

            user=user_obj,
            gold_stock=0.0,
            money_stock=data['money_amount']

        )
        wallet_obj.save()

    return {

        'responseEN': 'successfully change ...',
        'responseFA': 'تغییرات با موفقیت اعمال شد',

    }, 200
