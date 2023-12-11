import json

from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser

from API.AdminDashboard_DeskPage.post_param import UserChangeGoldAmountParam, UserChangeMoneyAmountParam
from API.AdminDashboard_DeskPage.utils import user_information_list, user_change_gold_amount, user_change_money_amount


class UsersInformationList(GenericAPIView):

    """

        return all user's information / اطلاعات تمامی کاربران سایت را میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):

        data = user_information_list()

        return JsonResponse(data, status=200)


class UserChangeGoldAmount(GenericAPIView):

    """

        change users wallets gold amount / مقدار موجودی طلا در کیف پول را تغییر میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = UserChangeGoldAmountParam

    def post(self, requesst):

        data = json.loads(requesst.body)
        data, status = user_change_gold_amount(data)

        return JsonResponse(data=data, status=status)


class UserChangeMoneyAmount(GenericAPIView):

    """

        change users wallets money amount / مقدار موجودی پول در کیف پول را تغییر میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = UserChangeMoneyAmountParam

    def post(self, requesst):

        data = json.loads(requesst.body)
        data, status = user_change_money_amount(data)

        return JsonResponse(data=data, status=status)
