import random

from django.contrib.auth.models import User
from django.utils import timezone

from LIB.utils import get_user_from_token
from SmsService.SMS import *
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

            'response-en': 'successfully code sent',
            'response-fa': 'کد با موفقیت ارسال شد',

        }, 200

    else:

        return {

            'response-en': 'code cant send',
            'response-fa': 'کد نمیتواند ارسال شود',

        }, 400


def prove_code(phone_number, code):

    try:

        user_obj = user_model.UserInformation.objects.get(user__username=phone_number)

    except:

        return {

            'response-en': 'user not found ',
            'response-fa': 'کاربری با این شماره موبایل یافت نشد'

        }, 404

    if timezone.now() <= (user_obj.auth_temp_code_create_date + datetime.timedelta(minutes=5)):

        if code == user_obj.auth_temp_code:

            try:
                token_key = Token.objects.get(user=user_obj.user).key
            except:
                token_key = Token.objects.create(user=user_obj.user).key

            return {

                'response-en': 'successfully code proved ...',
                'response-fa': 'کد با موفقیت تایید شد ...',
                'token': token_key,
                'user_type': user_obj.user_type,

            }, 200

        else:

            return {

                'response-en': 'wrong code',
                'response-fa': 'کد وارد شده اشتباه است ...',

            }, 400

    else:

        return {

            'response-en': 'code out of date',
            'response-fa': 'خارج از محدوده زمانی ...',

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

            'response-en': 'successfully user update ...',
            'response-fa': 'اطلاعات کاربر با موفقیت ثبت شد'

        }, 200

    else:

        return {

            'response-en': 'user not found ...',
            'response-fa': 'کاربر یافت نشد ...'

        }, 404


