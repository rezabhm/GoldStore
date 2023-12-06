from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from API.UserDashboard_DeskPage.utils import wallet_data


class WalletData(APIView):

    """

        return user's wallet's data / اطلاعات کیف پول کاربر را میدهد

    """

    allowed_methods = ('GET',)
    permission_classes = [IsAuthenticated]
    parser_classes = [TokenAuthentication]

    def get(self, request):

        data, status = wallet_data(request.auth)

        return JsonResponse(data, status=status)
