import json

from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from API.AdminDashboard_GetRequest.post_param import ProveMoneyGetRequestPostParam
from API.AdminDashboard_GetRequest.serializer import MoneyGetRequestSerializer
from API.AdminDashboard_GetRequest.utils import add_user_inf, prove_money_get_request
from Core.models.request import MoneyGetRequest


class MoneyGetRequestList(APIView):

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('GET',)

    def get(self, request):

        all_request = MoneyGetRequest.objects.all()
        all_request_serializer = MoneyGetRequestSerializer(data=all_request, many=True)
        all_request_serializer.is_valid()
        all_request_data = add_user_inf(all_request_serializer.data)

        un_accept_request = MoneyGetRequest.objects.filter(request_status=False)
        un_accept_request_serializer = MoneyGetRequestSerializer(data=un_accept_request, many=True)
        un_accept_request_serializer.is_valid()
        un_accept_request_data = add_user_inf(un_accept_request_serializer.data)

        return JsonResponse(data={

            'all_request': all_request_data,
            'un_accept_request': un_accept_request_data

        }, status=200)


class ProveMoneyGetRequest(GenericAPIView):

    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]
    allowed_methods = ('POST',)
    serializer_class = ProveMoneyGetRequestPostParam

    def post(self, request):

        req_data = json.loads(request.body)
        data, status = prove_money_get_request(get_req_id=req_data['get_request_id'])

        return JsonResponse(data=data, status=status)

