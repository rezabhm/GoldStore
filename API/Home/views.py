from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .utils import *


class GoldStockPrice(APIView):

    """

        we will return golds buy/sale price / قیمت خرید و فروش طلا را میدهد

    """

    allowed_methods = ('GET',)
    permission_classes = [AllowAny]

    def get(self, request):

        # get price from database
        data, status = get_gold_stock_price()

        return JsonResponse(data, status=status)


class ValidateToken(APIView):

    """

        in this api we will validate token / در این api توکن را اعتبار سنجی میکنیم

    """

    allowed_methods = ('GET',)
    permission_classes = (IsAuthenticated,)
    parser_classes = [TokenAuthentication]

    def get(self, request):

        return JsonResponse({

            'response-en': 'token is valid',
            'response-fa': 'توکن معتبر میباشد',

        }, status=202)
