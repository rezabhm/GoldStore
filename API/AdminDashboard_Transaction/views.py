from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from API.AdminDashboard_Transaction.serializer import TransactionSerializer
from API.AdminDashboard_Transaction.utils import add_user_inf
from Core.models.payment import PaymentTransactions


class TransactionList(APIView):

    """

        return all users transaction / تمامی تراکنش های واریزی کاربران را میدهد

    """

    allowed_methods = ('GET',)
    permission_classes = [IsAdminUser]
    parser_classes = [TokenAuthentication]

    def get(self, request):

        transaction_list = PaymentTransactions.objects.all()
        transaction_list_serializer = TransactionSerializer(data=transaction_list, many=True)
        transaction_list_serializer.is_valid()

        data = add_user_inf(transaction_list.data)

        return JsonResponse(data=data, status=200)