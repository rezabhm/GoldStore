from rest_framework import serializers

from Core.models.payment import PaymentTransactions
from Core.models.request import GoldGetRequest, MoneyGetRequest
from Core.models.stock import BuyGold, SaleGold


class BuyReportingSerializer(serializers.ModelSerializer):

    class Meta:

        model = BuyGold
        fields = [

            'buy_date',
            'money_amount',
            'gold_amount',
            'request_status',

        ]


class SaleReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleGold
        fields = [

            'sale_date',
            'money_amount',
            'gold_amount',
            'request_status',

        ]


class GoldGetRequestReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldGetRequest
        fields = [

            'request_date',
            'gold_amount',
            'request_status',

        ]


class MoneyGetRequestReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyGetRequest
        fields = [

            'request_date',
            'money_amount',
            'request_status',

        ]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransactions
        fields = [

            'payment_date',
            'money_amount',
            'status',

        ]
