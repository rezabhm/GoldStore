import random

from django.contrib.auth.models import User
from django.utils import timezone

from LIB.utils import get_user_from_token
from LIB.SmsService.SMS import *
from Core.models import user as user_model
from rest_framework.authtoken.models import Token

import datetime


def send_code(phone_number):

    code = str(random.randint(100000, 999999))

    try:

        user_obj = User.objects.get(username=phone_number)
        user_inf = user_model.UserInformation.objects.get(user=user_obj)

        user_inf.auth_temp_code = code
        user_inf.auth_temp_code_create_date = timezone.now()

        user_inf.save()

    except:

        user_obj = User(username=phone_number)
        user_obj.save()

        user_inf = user_model.UserInformation(

            user=user_obj,
            joined_date=timezone.now(),
            national_code='',
            auth_temp_code=code,
            auth_temp_code_create_date=timezone.now()


        )

        user_inf.save()

    status, _ = send_password_code_sms(phone_number, code)

    if status:

        msg = 'کاربرگرامی برای ورودکد زیر را وارد نمایید'

        sms_obj = user_model.SmsMSG(

            user=user_obj,
            message=msg,
            sendDate=timezone.now()

        )

        sms_obj.save()

        return {

            'responseEN': 'successfully code sent',
            'responseFA': 'کد با موفقیت ارسال شد',

        }, 200

    else:

        return {

            'responseEN': 'code cant send',
            'responseFA': 'کد نمیتواند ارسال شود',

        }, 400


def prove_code(phone_number, code):

    try:

        user_obj = user_model.UserInformation.objects.get(user__username=phone_number)

    except:

        return {

            'responseEN': 'user not found ',
            'responseFA': 'کاربری با این شماره موبایل یافت نشد'

        }, 404

    if timezone.now() <= (user_obj.auth_temp_code_create_date + datetime.timedelta(minutes=5)):

        if code == user_obj.auth_temp_code:

            try:
                token_key = Token.objects.get(user=user_obj.user).key
            except:
                token_key = Token.objects.create(user=user_obj.user).key

            return {

                'responseEN': 'successfully code proved ...',
                'responseFA': 'کد با موفقیت تایید شد ...',
                'token': token_key,
                'user_type': user_obj.user_type,
                'signup_require': True if user_obj.national_code == '' else False

            }, 200

        else:

            return {

                'responseEN': 'wrong code',
                'responseFA': 'کد وارد شده اشتباه است ...',

            }, 400

    else:

        return {

            'responseEN': 'code out of date',
            'responseFA': 'خارج از محدوده زمانی ...',

        }, 400


def signup_user(token_key, data):

    user_status, user_obj, user_inf = get_user_from_token(token_key)

    if user_status:

        user_obj.first_name = data['first_name']
        user_obj.last_name = data['last_name']
        user_obj.email = data['email']

        user_obj.save()

        user_inf.national_code = data['national_code']
        user_inf.joined_date = timezone.now()

        user_inf.save()

        return {

            'responseEN': 'successfully user update ...',
            'responseFA': 'اطلاعات کاربر با موفقیت ثبت شد'

        }, 200

    else:

        return {

            'responseEN': 'user not found ...',
            'responseFA': 'کاربر یافت نشد ...'

        }, 404


