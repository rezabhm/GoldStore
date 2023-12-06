from rest_framework import serializers


class GetRequestMoneySerializer(serializers.Serializer):

    money_amount = serializers.FloatField()


class GetRequestGoldSerializer(serializers.Serializer):

    gold_amount = serializers.FloatField()
