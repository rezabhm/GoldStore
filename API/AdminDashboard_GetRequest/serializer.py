from rest_framework import serializers

from Core.models.request import MoneyGetRequest, GoldGetRequest


class MoneyGetRequestSerializer(serializers.ModelSerializer):

    class Meta:

        model = MoneyGetRequest
        fields = '__all__'


class GoldGetRequestSerializer(serializers.ModelSerializer):

    class Meta:

        model = GoldGetRequest
        fields = '__all__'
