import json

from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from API.UserDashboard_GoldBuySale import utils
from API.UserDashboard_GoldBuySale.post_param import SaleGold, BuyGold


class SaleGoldRequest(GenericAPIView):

    """

        request to sale gold / درخواست فروش طلا

    """

    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = SaleGold

    def post(self, request):

        req_data = json.loads(request.body)
        data, status = utils.sale_gold(request.auth, req_data['gold_amount'])

        return JsonResponse(data, status=status)


class BuyGoldRequest(GenericAPIView):

    """

        request to buy gold / درخواست خرید طلا

    """

    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = BuyGold

    def post(self, request):

        req_data = json.loads(request.body)
        data, status = utils.buy_gold(request.auth, req_data['gold_amount'])

        return JsonResponse(data, status=status)
