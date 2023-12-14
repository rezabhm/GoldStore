from rest_framework import serializers


class ChangeMoneyPostParam(serializers.Serializer):

    gold_price = serializers.FloatField()


class ChangeGoldAmountParam(serializers.Serializer):

    gold_amount = serializers.FloatField()


class PriceDifferenceParam(serializers.Serializer):

    price_difference = serializers.FloatField()
