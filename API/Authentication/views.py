import json

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from . import utils


class SendCode(APIView):

    """

        send code to user for sign-up with temporary code / ارسال کد به کاربر برای ثبت نام و لاگین

    """

    permission_classes = [AllowAny]
    allowed_methods = ('GET',)

    def get(self, requests, phone_number):

        data, status = utils.send_code(phone_number)

        return JsonResponse(data, status=status)


class ProveCode(APIView):

    """

        proved login/sign-up code / تایید کد ورود کاربر

    """

    permission_classes = (AllowAny,)
    allowed_methods = ('POST',)

    def post(self, request):

        req_data = json.loads(request.body)
        data, status = utils.prove_code(req_data['phone_number'], req_data['code'])

        return JsonResponse(data, status=status)


class SignUp(APIView):
    """

        sign-up user with users information / ثبت نام کاربر

    """

    permission_classes = [IsAuthenticated]
    allowed_methods = ('POST',)
    parser_classes = [TokenAuthentication]

    def post(self, request):

        req_data = json.loads(request.body)
        data, status = utils.signup_user(request.auth, req_data)

        return JsonResponse(data, status=status)
