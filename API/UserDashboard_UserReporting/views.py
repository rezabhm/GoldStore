from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from API.UserDashboard_UserReporting.serializer import BuyReportingSerializer, SaleReportingSerializer, \
    GoldGetRequestReportingSerializer, MoneyGetRequestReportingSerializer, TransactionSerializer
from API.UserDashboard_UserReporting.utils import change_status, change_date_buy_gold, change_date_sale_gold, \
    change_date_get_request, change_date_transaction
from Core.models.payment import PaymentTransactions
from Core.models.request import GoldGetRequest, MoneyGetRequest
from Core.models.stock import SaleGold, BuyGold
from LIB.utils import get_user_from_token


class BuyGoldReport(GenericAPIView):
    """

        user buying gold stock / گزارش دهی خرید طلا برای کاربر

    """

    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):
        _, user, _ = get_user_from_token(request.auth)
        buy_gold_report_list = BuyGold.objects.filter(user=user).order_by('buy_date').reverse()
        buy_gold_report_serializer = BuyReportingSerializer(data=buy_gold_report_list, many=True)
        buy_gold_report_serializer.is_valid()
        data = change_status(buy_gold_report_serializer.data)
        data = change_date_buy_gold(data)

        return JsonResponse(data={"data": data}, status=200)


class SaleGoldReport(GenericAPIView):
    """

        user sale gold stock / گزارش دهی فروش طلا برای کاربر

    """

    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):

        _, user, _ = get_user_from_token(request.auth)
        sale_gold_report_list = SaleGold.objects.filter(user=user).order_by('sale_date').reverse()
        sale_gold_report_serializer = SaleReportingSerializer(data=sale_gold_report_list, many=True)
        sale_gold_report_serializer.is_valid()
        data = change_status(sale_gold_report_serializer.data)
        data = change_date_sale_gold(data)

        return JsonResponse(data={"data": data}, status=200)


class GetGoldRequestReport(GenericAPIView):
    """

        user get gold request report / گزارش دهی درخواست طلا

    """

    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):
        _, user, _ = get_user_from_token(request.auth)
        gold_get_request_report_list = GoldGetRequest.objects.filter(user=user).order_by('request_date').reverse()
        gold_get_request_report_serializer = GoldGetRequestReportingSerializer(data=gold_get_request_report_list,
                                                                               many=True)
        gold_get_request_report_serializer.is_valid()
        data = change_status(gold_get_request_report_serializer.data)
        data = change_date_get_request(data)

        return JsonResponse(data={"data": data}, status=200)


class GetMoneyRequestReport(GenericAPIView):
    """

        user get money request report / گزارش دهی درخواست برداشت وجه

    """

    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):
        _, user, _ = get_user_from_token(request.auth)
        money_get_request_report_list = MoneyGetRequest.objects.filter(user=user).order_by('request_date').reverse()
        money_get_request_report_serializer = MoneyGetRequestReportingSerializer(data=money_get_request_report_list,
                                                                                 many=True)
        money_get_request_report_serializer.is_valid()
        data = change_status(money_get_request_report_serializer.data)
        data = change_date_get_request(data)

        return JsonResponse(data={"data": data}, status=200)


class TransactionReport(GenericAPIView):
    """

        user transaction report / گزارش دهی تراکنش های کاربر

    """

    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):
        _, user, _ = get_user_from_token(request.auth)
        transaction_report_list = PaymentTransactions.objects.filter(user=user).order_by('payment_date').reverse()
        transaction_report_serializer = TransactionSerializer(data=transaction_report_list,
                                                              many=True)
        transaction_report_serializer.is_valid()
        data = change_date_transaction(transaction_report_serializer.data)

        return JsonResponse(data={"data": data}, status=200)
