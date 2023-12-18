import json

from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from API.AdminDashboard_GetRequest.post_param import ProveMoneyGetRequestPostParam, ProveGoldGetRequestPostParam
from API.AdminDashboard_GetRequest.serializer import MoneyGetRequestSerializer, GoldGetRequestSerializer
from API.AdminDashboard_GetRequest.utils import add_user_inf, prove_money_get_request, prove_gold_get_request
from Core.models.request import MoneyGetRequest, GoldGetRequest


class MoneyGetRequestList(APIView):

    """

        all users money get requests list / تمامی درخواست های برداشت وجه کاربران را میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):

        all_request = MoneyGetRequest.objects.all().order_by('request_date').reverse()
        all_request_serializer = MoneyGetRequestSerializer(data=all_request, many=True)
        all_request_serializer.is_valid()
        all_request_data = add_user_inf(all_request_serializer.data)

        un_accept_request = MoneyGetRequest.objects.filter(request_status='waiting').order_by('request_date').reverse()
        un_accept_request_serializer = MoneyGetRequestSerializer(data=un_accept_request, many=True)
        un_accept_request_serializer.is_valid()
        un_accept_request_data = add_user_inf(un_accept_request_serializer.data)

        return JsonResponse(data={

            'all_request': all_request_data,
            'un_accept_request': un_accept_request_data

        }, status=200)


class ProveMoneyGetRequest(GenericAPIView):

    """

        admin prove users money get request / تایید درخواست برداشت وجه توسط ادمین

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = ProveMoneyGetRequestPostParam

    def post(self, request):

        req_data = json.loads(request.body)
        data, status = prove_money_get_request(get_req_id=req_data['get_request_id'], request_type=req_data['request_type'])

        return JsonResponse(data=data, status=status)


class GoldGetRequestList(APIView):
    """

        all users gold get requests list / تمامی درخواست های برداشت طلای کاربران را میدهد

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):
        all_request = GoldGetRequest.objects.all().order_by('request_date').reverse()
        all_request_serializer = GoldGetRequestSerializer(data=all_request, many=True)
        all_request_serializer.is_valid()
        all_request_data = add_user_inf(all_request_serializer.data)

        un_accept_request = GoldGetRequest.objects.filter(request_status='waiting').order_by('request_date').reverse()
        un_accept_request_serializer = GoldGetRequestSerializer(data=un_accept_request, many=True)
        un_accept_request_serializer.is_valid()
        un_accept_request_data = add_user_inf(un_accept_request_serializer.data)

        return JsonResponse(data={

            'all_request': all_request_data,
            'un_accept_request': un_accept_request_data

        }, status=200)


class ProveGoldGetRequest(GenericAPIView):

    """

        admin prove users gold get request / تایید درخواست برداشت طلا توسط ادمین

    """

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = ProveGoldGetRequestPostParam

    def post(self, request):

        req_data = json.loads(request.body)
        data, status = prove_gold_get_request(get_req_id=req_data['get_request_id'], request_type=req_data['request_type'])

        return JsonResponse(data=data, status=status)
