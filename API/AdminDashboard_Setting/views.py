import json

from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from API.AdminDashboard_Setting.post_param import ChangeMoneyPostParam, ChangeGoldAmountParam, PriceDifferenceParam
from API.AdminDashboard_Setting.serializer import GoldPriceSerializer
from API.AdminDashboard_Setting.utils import change_gold_price, open_close_stock, change_store_gold_amount, \
    change_price_difference
from Core.models.gold import GoldPrice


class SettingData(APIView):

    """

        get settings data / اطلاعات تنظیمات را دریافت میکند

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):

        try:

            gold_obj = GoldPrice.objects.filter(active=True).order_by('Date')
            gold_serializer = GoldPriceSerializer(data=gold_obj, many=True)
            gold_serializer.is_valid()

            return JsonResponse(data={'data': gold_serializer.data[-1]}, status=200)

        except:

            return JsonResponse(data={

                'responseEN': 'setting didn\'t add',
                'responseFA': 'تنظیمات اعمال نشده است',

            }, status=400)


class ChangePrice(GenericAPIView):

    """

        change gold price / قیمت طلا را تفییر میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = ChangeMoneyPostParam

    def post(self, request):

        req_data = json.loads(request.body)
        data, status = change_gold_price(req_data['gold_price'])

        return JsonResponse(data=data, status=status)


class OpenCloseStock(APIView):

    """

        open/close stock / بازار را باز میکند یا میبندد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):

        data, status = open_close_stock()

        return JsonResponse(data=data, status=status)


class ChangeStoreGoldAmount(GenericAPIView):

    """

        change stores gold amount / میزان موجودی طلا در انبار مغازه را تفییر میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = ChangeGoldAmountParam

    def post(self, request):

        req_data = json.load(request.body)
        data, status = change_store_gold_amount(gold_amount=req_data['gold_amount'])

        return JsonResponse(data=data, status=status)


class PriceDifference(GenericAPIView):

    """

        change buy/sale price difference / اختلاف قیمت خرید و فروش طلا را تفییر میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = PriceDifferenceParam

    def post(self, request):

        req_data = json.load(request.body)
        data, status = change_price_difference(price_difference=req_data['price_difference'])

        return JsonResponse(data=data, status=status)
