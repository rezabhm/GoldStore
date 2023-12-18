import json

from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from API.AdminDashboard_BuySale.post_param import ProveSaleReqeustParam
from API.AdminDashboard_BuySale.serializer import SaleGoldSerializer, BuyGoldSerializer
from API.AdminDashboard_BuySale.utils import add_inf, add_inf_buy, prove_sale_request
from Core.models.stock import SaleGold, BuyGold


class SaleList(APIView):

    """

        return all users sale  gold request list / لیست تمای درخواست های فروش طلا توسط مشتری را میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):

        all_sale_gold_list = SaleGold.objects.all().order_by('sale_date').reverse()
        all_sale_gold_serializer = SaleGoldSerializer(data=all_sale_gold_list, many=True)
        all_sale_gold_serializer.is_valid()
        all_sale_gold_list = add_inf(all_sale_gold_serializer.data)

        unacceptable_sale_gold_list = SaleGold.objects.filter(request_status='waiting').order_by('sale_date').reverse()
        unacceptable_sale_gold_serializer = SaleGoldSerializer(data=unacceptable_sale_gold_list, many=True)
        unacceptable_sale_gold_serializer.is_valid()
        unacceptable_sale_gold_list = add_inf(unacceptable_sale_gold_serializer.data)

        return JsonResponse(data={

                    'data': all_sale_gold_list,
                    'unacceptable_data': unacceptable_sale_gold_list

                }, status=200
            )


class BuyList(APIView):

    """

        return all users buy  gold request list / لیست تمای درخواست های خرید طلا توسط مشتری را میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):

        all_buy_gold_list = BuyGold.objects.all().order_by('buy_date').reverse()
        all_buy_gold_serializer = BuyGoldSerializer(data=all_buy_gold_list, many=True)
        all_buy_gold_serializer.is_valid()
        all_buy_gold_list = add_inf_buy(all_buy_gold_serializer.data)

        return JsonResponse(data={

              'data': all_buy_gold_list,

             }, status=200
        )


class ProveSaleRequest(GenericAPIView):

    """

        prove users gold sale request / تایید درخواست فروش طلا

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = ProveSaleReqeustParam

    def post(self, request):

        req_data = json.loads(request.body)
        data, status = prove_sale_request(req_data['sale_request_id'], req_data['prove_status'])

        return JsonResponse(data=data, status=status)
