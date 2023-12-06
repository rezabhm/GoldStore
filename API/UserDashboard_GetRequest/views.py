import json

from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from API.UserDashboard_GetRequest.post_param import GetRequestMoneySerializer, GetRequestGoldSerializer
from API.UserDashboard_GetRequest.utils import get_request_money, get_request_gold


class GetRequestMoney(GenericAPIView):

    """

        user request for get money from wallet / درخواست برداشت وحه از کیف پول

    """

    allowed_method = ('POST',)
    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]
    serializer_class = GetRequestMoneySerializer

    def post(self, request):

        req_body = json.loads(request.body)
        data, status = get_request_money(request.auth, float(req_body['money_amount']))

        return JsonResponse(data, status=status)


class GetRequestGold(GenericAPIView):

    """

        user request for get gold from wallet / درخواست برداشت طلا از کیف پول

    """

    allowed_method = ('POST',)
    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]
    serializer_class = GetRequestGoldSerializer

    def post(self, request):

        req_body = json.loads(request.body)
        data, status = get_request_gold(request.auth, float(req_body['gold_amount']))

        return JsonResponse(data, status=status)
