from rest_framework import serializers

from Core.models.request import MoneyGetRequest


class MoneyGetRequestSerializer(serializers.ModelSerializer):

    class Meta:

        model = MoneyGetRequest
        fields = '__all__'
