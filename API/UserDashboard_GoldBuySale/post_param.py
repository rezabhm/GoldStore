from rest_framework import serializers


class SaleGold(serializers.Serializer):

    gold_amount = serializers.FloatField()


class BuyGold(serializers.Serializer):

    gold_amount = serializers.FloatField()
