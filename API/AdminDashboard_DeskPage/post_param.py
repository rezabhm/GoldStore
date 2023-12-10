from rest_framework import serializers


class UserChangeGoldAmountParam(serializers.Serializer):

    phone_number = serializers.CharField()
    gold_amount = serializers.FloatField()


class UserChangeMoneyAmountParam(serializers.Serializer):
    phone_number = serializers.CharField()
    money_amount = serializers.FloatField()
